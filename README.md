# VFN Preprocessing

Preprocessing of different file formats for chunking and RAG. This tool compares different document processing libraries to convert unstructured documents (like PDFs) into structured Markdown format.

## Features

- **Multiple Converter Support**: Compare four different document processing libraries:
  - **Unstructured.io**: Advanced document parsing with element detection and formula handling
  - **MarkItDown**: Microsoft's document-to-markdown converter
  - **Docling**: IBM's document understanding and conversion tool
  - **Mistral**: Direct LLM-based markdown parsing using Mistral Document AI API

- **Formula Support**: Mathematical formulas are automatically converted to LaTeX format in Markdown (inline `$...$` for short formulas, display `$$...$$` for longer equations)

- **Wide Format Support**: Process various document types including PDF, DOCX, PPTX, XLSX, HTML, and more

- **Easy Comparison**: Run multiple converters on the same document and compare results

- **Command-Line Interface**: Simple CLI for quick document processing and comparison

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

### Prerequisites

- Python 3.10 or higher
- Poetry (install with `pip install poetry`)

### Environment Variables

Some converters require API keys. Create a `.env` file in the project root with the following format:

```bash
# Unstructured.io API key (optional - for cloud API usage)
UNSTRUCTURED_API_KEY=""

# Mistral API credentials (required for Mistral converter)
# Get these from the Azure Portal
MISTRAL_API_URL=""
MISTRAL_API_KEY=""
```

**Note**: The Mistral API URL and key come from the Azure Portal when you set up Mistral AI services.

### Install Dependencies

```bash
# Install all dependencies
poetry install

# Activate the virtual environment
poetry shell
```

## Usage

### Command-Line Interface

The package provides a `vfn-preprocess` command with three main subcommands:

#### 1. Convert a Single Document

Convert a document using a specific converter:

```bash
vfn-preprocess convert input.pdf output.md --converter unstructured
```

Available converters:
- `unstructured` - Unstructured.io
- `markitdown` - MarkItDown
- `docling` - Docling
- `mistral` - Mistral Document AI API

#### 2. Compare Multiple Converters

Run all compatible converters on a document and compare results:

```bash
# Compare all compatible converters
vfn-preprocess compare input.pdf

# Compare specific converters
vfn-preprocess compare input.pdf -c unstructured -c markitdown

# Specify output directory
vfn-preprocess compare input.pdf --output-dir ./results
```

This will:
- Run each converter on the input document
- Save outputs with converter-specific names
- Display a comparison table with timing and success metrics

#### 3. List Available Converters

View all available converters and their supported formats:

```bash
vfn-preprocess list-converters
```

### Programmatic Usage

You can also use the converters directly in Python code:

```python
from pathlib import Path
from vfn_preprocessing import UnstructuredConverter, MarkitdownConverter, DoclingConverter, MistralConverter

# Initialize a converter
converter = UnstructuredConverter()

# Or use Mistral for LLM-based conversion
# converter = MistralConverter()  # Requires MISTRAL_API_KEY and MISTRAL_API_URL in .env

# Check format support
if converter.supports_format('.pdf'):
    # Convert document
    result = converter.convert(
        input_path=Path('document.pdf'),
        output_path=Path('output.md')
    )
    
    if result['success']:
        print(f"Conversion took {result['time_seconds']:.2f} seconds")
    else:
        print(f"Error: {result['error']}")
```

## Supported Formats

### Unstructured.io
- Documents: PDF, DOCX, DOC, PPTX, PPT, XLSX, XLS, RTF, ODT, EPUB
- Web: HTML, XML, EML, MSG
- Text: TXT

### MarkItDown
- Documents: PDF, DOCX, PPTX, XLSX
- Images: JPG, JPEG, PNG, GIF
- Web: HTML, HTM
- Data: CSV, JSON, XML
- Archives: ZIP
- Audio: WAV, MP3
- Text: TXT

### Docling
- Documents: PDF, DOCX, PPTX, XLSX
- Images: PNG, JPG, JPEG
- Web: HTML
- Text: ASCIIDOC, MD

### Mistral
- Documents: PDF, DOCX, PPTX, XLSX
- Images: JPG, JPEG, PNG

## Development

### Running Tests

```bash
# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=vfn_preprocessing

# Run specific test file
poetry run pytest tests/test_converters.py
```

### Code Formatting

```bash
# Format code with black
poetry run black vfn_preprocessing tests

# Lint with ruff
poetry run ruff check vfn_preprocessing tests
```

## Project Structure

```
vfn-preprocessing/
├── vfn_preprocessing/          # Main package
│   ├── __init__.py            # Package initialization
│   ├── base.py                # Base converter class
│   ├── cli.py                 # Command-line interface
│   ├── unstructured_converter.py   # Unstructured.io implementation
│   ├── markitdown_converter.py     # MarkItDown implementation
│   ├── docling_converter.py        # Docling implementation
│   └── mistral_converter.py        # Mistral Document AI implementation
├── tests/                     # Test suite
│   ├── test_base.py          # Base class tests
│   └── test_converters.py    # Converter tests
├── examples/                  # Example documents (add your test files here)
├── pyproject.toml            # Poetry configuration
└── README.md                 # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is part of Deltares Research.

## Acknowledgments

This tool integrates the following libraries and services:
- [Unstructured.io](https://github.com/Unstructured-IO/unstructured)
- [MarkItDown](https://github.com/microsoft/markitdown)
- [Docling](https://github.com/DS4SD/docling)
- [Mistral AI](https://mistral.ai/) - Document AI API for LLM-based conversion
