"""Command-line interface for VFN preprocessing."""

import sys
from pathlib import Path
from typing import List, Optional

import click
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

from vfn_preprocessing import (
    UnstructuredConverter,
    MarkitdownConverter,
    DoclingConverter,
)

console = Console()


def get_all_converters():
    """Get all available converters."""
    return [
        UnstructuredConverter(),
        MarkitdownConverter(),
        DoclingConverter(),
    ]


def get_converter_by_name(name: str):
    """Get a converter by name."""
    converters = {
        "unstructured": UnstructuredConverter,
        "markitdown": MarkitdownConverter,
        "docling": DoclingConverter,
    }
    converter_class = converters.get(name.lower())
    if converter_class:
        return converter_class()
    return None


@click.group()
@click.version_option(version="0.1.0")
def main():
    """VFN Preprocessing - Convert documents to markdown using different libraries."""
    pass


@main.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=Path))
@click.argument("output_file", type=click.Path(path_type=Path))
@click.option(
    "--converter",
    "-c",
    type=click.Choice(["unstructured", "markitdown", "docling"], case_sensitive=False),
    required=True,
    help="Converter to use for processing",
)
def convert(input_file: Path, output_file: Path, converter: str):
    """Convert a single document to markdown.
    
    Example:
        vfn-preprocess convert input.pdf output.md --converter unstructured
    """
    converter_obj = get_converter_by_name(converter)
    if not converter_obj:
        console.print(f"[red]Error:[/red] Unknown converter '{converter}'")
        sys.exit(1)

    # Check if format is supported
    file_ext = input_file.suffix
    if not converter_obj.supports_format(file_ext):
        console.print(
            f"[red]Error:[/red] {converter_obj.name} does not support {file_ext} files"
        )
        sys.exit(1)

    console.print(f"[cyan]Converting {input_file.name} using {converter_obj.name}...[/cyan]")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Processing...", total=None)
        result = converter_obj.convert(input_file, output_file)

    if result["success"]:
        console.print(f"[green]✓[/green] Conversion successful!")
        console.print(f"  Output: {result['output_path']}")
        console.print(f"  Time: {result['time_seconds']:.2f}s")
    else:
        console.print(f"[red]✗[/red] Conversion failed!")
        console.print(f"  Error: {result.get('error', 'Unknown error')}")
        sys.exit(1)


@main.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--output-dir",
    "-o",
    type=click.Path(path_type=Path),
    default=None,
    help="Output directory (default: same as input with _output suffix)",
)
@click.option(
    "--converters",
    "-c",
    multiple=True,
    type=click.Choice(["unstructured", "markitdown", "docling"], case_sensitive=False),
    help="Specific converters to use (default: all compatible)",
)
def compare(input_file: Path, output_dir: Optional[Path], converters: tuple):
    """Compare multiple converters on the same document.
    
    Example:
        vfn-preprocess compare input.pdf
        vfn-preprocess compare input.pdf -c unstructured -c markitdown
    """
    # Determine output directory
    if output_dir is None:
        output_dir = input_file.parent / f"{input_file.stem}_output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get converters to use
    if converters:
        converter_objs = [get_converter_by_name(c) for c in converters]
        converter_objs = [c for c in converter_objs if c is not None]
    else:
        converter_objs = get_all_converters()

    # Filter converters by file format support
    file_ext = input_file.suffix
    compatible_converters = [
        c for c in converter_objs if c.supports_format(file_ext)
    ]

    if not compatible_converters:
        console.print(f"[red]Error:[/red] No converters support {file_ext} files")
        sys.exit(1)

    console.print(f"[cyan]Comparing converters on {input_file.name}[/cyan]")
    console.print(f"Compatible converters: {', '.join(c.name for c in compatible_converters)}\n")

    results = []
    
    for converter in compatible_converters:
        output_file = output_dir / f"{input_file.stem}_{converter.name.lower().replace('.', '_').replace(' ', '_')}.md"
        
        console.print(f"[yellow]Running {converter.name}...[/yellow]")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task(f"Processing with {converter.name}...", total=None)
            result = converter.convert(input_file, output_file)
        
        results.append(result)
        
        if result["success"]:
            console.print(f"  [green]✓[/green] Success in {result['time_seconds']:.2f}s")
        else:
            console.print(f"  [red]✗[/red] Failed: {result.get('error', 'Unknown error')}")
        console.print()

    # Display comparison table
    table = Table(title="Conversion Results Comparison")
    table.add_column("Converter", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Time (s)", justify="right", style="green")
    table.add_column("Output File", style="blue")

    for result in results:
        status = "✓ Success" if result["success"] else "✗ Failed"
        status_style = "green" if result["success"] else "red"
        time_str = f"{result['time_seconds']:.2f}"
        output_str = Path(result['output_path']).name if result["success"] else "-"
        
        table.add_row(
            result["converter"],
            f"[{status_style}]{status}[/{status_style}]",
            time_str,
            output_str,
        )

    console.print(table)
    console.print(f"\n[cyan]Output directory:[/cyan] {output_dir}")


@main.command()
def list_converters():
    """List all available converters and their supported formats."""
    converters = get_all_converters()
    
    table = Table(title="Available Converters")
    table.add_column("Name", style="cyan")
    table.add_column("Class", style="magenta")
    table.add_column("Supported Formats", style="green")

    for converter in converters:
        formats = ", ".join(sorted(converter._supported_formats))
        info = converter.get_info()
        table.add_row(info["name"], info["class"], formats)

    console.print(table)


if __name__ == "__main__":
    main()
