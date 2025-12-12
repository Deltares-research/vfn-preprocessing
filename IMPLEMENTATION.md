# VFN Preprocessing Implementation Summary

## Overview

This project implements a Python application for preprocessing unstructured documents and converting them to structured Markdown format. The application uses Poetry for package management and integrates four document processing libraries for comparison purposes, including an LLM-based converter.

## Implemented Features

### 1. Document Converter Architecture

A clean, extensible architecture with:
- **Base Interface**: `DocumentConverter` abstract base class defining the converter contract
- **Four Implementations**:
  - `UnstructuredConverter` - Using Unstructured.io library
  - `MarkitdownConverter` - Using Microsoft's MarkItDown library
  - `DoclingConverter` - Using IBM's Docling library
  - `MistralConverter` - Using Mistral Document AI API for LLM-based conversion

### 2. Command-Line Interface (CLI)

A user-friendly CLI built with Click and Rich, featuring:

#### `vfn-preprocess convert`
Convert a single document using a specific converter:
```bash
vfn-preprocess convert input.pdf output.md --converter unstructured
```

#### `vfn-preprocess compare`
Compare multiple converters on the same document:
```bash
vfn-preprocess compare input.pdf
vfn-preprocess compare input.pdf -c unstructured -c markitdown
```

This command:
- Automatically detects compatible converters
- Runs each converter and measures performance
- Generates a comparison table with timing and success metrics
- Saves outputs with converter-specific names

#### `vfn-preprocess list-converters`
List all available converters and their supported formats:
```bash
vfn-preprocess list-converters
```

### 3. Supported File Formats

**Unstructured.io** (14 formats):
- Documents: PDF, DOCX, DOC, PPTX, PPT, XLSX, XLS, RTF, ODT, EPUB
- Web/Email: HTML, XML, EML, MSG
- Text: TXT

**MarkItDown** (17 formats):
- Documents: PDF, DOCX, PPTX, XLSX
- Images: JPG, JPEG, PNG, GIF
- Web/Data: HTML, HTM, CSV, JSON, XML
- Archives: ZIP
- Audio: WAV, MP3
- Text: TXT

**Docling** (7 formats):
- Documents: PDF, DOCX, PPTX
- Web: HTML
- Text: ASCIIDOC, MD, MARKDOWN

**Mistral** (6 formats):
- Documents: PDF, DOCX, PPTX, XLSX
- Images: JPG, JPEG, PNG

### 4. Testing

Comprehensive test suite covering:
- Base converter class functionality
- Converter initialization
- Format support detection
- Error handling

Run tests with:
```bash
poetry run pytest
poetry run pytest --cov=vfn_preprocessing  # With coverage
```

### 5. Code Quality

- **Formatting**: Black configured with 100-character line length
- **Linting**: Ruff for fast Python linting
- **Type Hints**: Used throughout the codebase
- **Documentation**: Comprehensive docstrings and README

### 6. Security

- ✅ All dependencies checked via GitHub Advisory Database - no vulnerabilities found
- ✅ CodeQL security analysis passed with 0 alerts
- ✅ Code review completed and all issues addressed

## Project Structure

```
vfn-preprocessing/
├── vfn_preprocessing/          # Main package
│   ├── __init__.py            # Package initialization
│   ├── base.py                # Base converter interface
│   ├── cli.py                 # CLI application
│   ├── unstructured_converter.py
│   ├── markitdown_converter.py
│   └── docling_converter.py
├── tests/                     # Test suite
│   ├── __init__.py
│   ├── test_base.py
│   └── test_converters.py
├── examples/                  # Example documents
│   ├── README.md             # Usage examples
│   └── sample.txt            # Sample document
├── pyproject.toml            # Poetry configuration
├── poetry.lock               # Locked dependencies
└── README.md                 # Main documentation
```

## Installation & Usage

### Quick Start

```bash
# Install Poetry (if not already installed)
pip install poetry

# Install dependencies
poetry install

# Activate virtual environment
poetry shell

# Try it out!
vfn-preprocess list-converters
vfn-preprocess compare examples/sample.txt
```

### Python API

```python
from pathlib import Path
from vfn_preprocessing import UnstructuredConverter, MarkitdownConverter, DoclingConverter

# Use a specific converter
converter = UnstructuredConverter()
result = converter.convert(
    input_path=Path('document.pdf'),
    output_path=Path('output.md')
)

if result['success']:
    print(f"Converted in {result['time_seconds']:.2f}s")
```

## Performance Characteristics

Based on testing with a sample text document:

| Converter       | Speed    | Output Quality | Best For |
|----------------|----------|----------------|----------|
| MarkItDown     | Fastest  | Clean, accurate | Quick conversions, wide format support |
| Unstructured.io| Medium   | Element-aware  | Complex documents, detailed extraction |
| Docling        | Slower   | High-quality   | PDFs, layout preservation |

*Note: Performance varies significantly based on document type and complexity*

## Key Design Decisions

1. **Abstract Base Class**: Ensures all converters implement a consistent interface
2. **Rich Terminal UI**: Provides excellent user feedback with progress indicators and tables
3. **Poetry**: Modern dependency management with reproducible builds
4. **Minimal Dependencies**: Only essential libraries, no unnecessary bloat
5. **Extensibility**: Easy to add new converters by inheriting from DocumentConverter

## Development Guidelines

### Adding a New Converter

1. Create a new file: `vfn_preprocessing/new_converter.py`
2. Inherit from `DocumentConverter`
3. Implement `convert()` and `supports_format()` methods
4. Add to `__init__.py` exports
5. Update CLI to include the new converter
6. Add tests in `tests/test_converters.py`

### Running Quality Checks

```bash
# Format code
poetry run black vfn_preprocessing tests

# Lint code
poetry run ruff check vfn_preprocessing tests

# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=vfn_preprocessing
```

## Future Enhancements

Potential improvements for future versions:

1. **Batch Processing**: Process entire directories of documents
2. **Output Formats**: Support additional output formats (HTML, JSON, etc.)
3. **Configuration Files**: Allow users to save converter preferences
4. **Parallel Processing**: Process multiple documents simultaneously
5. **Web Interface**: Add a web UI for easier access
6. **Docker Support**: Containerize the application
7. **Cloud Integration**: Support for S3, Google Cloud Storage, etc.
8. **Quality Metrics**: Analyze and score conversion quality
9. **Diff Tool**: Compare outputs from different converters
10. **Custom Converters**: Plugin system for user-defined converters

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure you're in the Poetry virtual environment (`poetry shell`)
2. **Missing Dependencies**: Run `poetry install` to install all dependencies
3. **Format Not Supported**: Use `vfn-preprocess list-converters` to check supported formats
4. **Conversion Failures**: Check the error message in the output; some converters may require additional system dependencies

## Contributing

When contributing to this project:

1. Follow the existing code style (Black formatting, 100-char lines)
2. Add tests for new functionality
3. Update documentation as needed
4. Run all quality checks before submitting
5. Ensure security scans pass

## License

This project is part of Deltares Research.

## Acknowledgments

This project integrates excellent open-source libraries:
- [Unstructured.io](https://github.com/Unstructured-IO/unstructured) - Document processing
- [MarkItDown](https://github.com/microsoft/markitdown) - Microsoft's conversion tool
- [Docling](https://github.com/DS4SD/docling) - IBM's document understanding
- [Click](https://click.palletsprojects.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting
- [Poetry](https://python-poetry.org/) - Dependency management
