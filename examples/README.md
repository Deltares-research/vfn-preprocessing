# Example Usage

This directory contains example documents and usage scenarios for testing the VFN preprocessing tool.

## Quick Start Examples

### 1. Convert a PDF Document

```bash
# Using Unstructured.io
vfn-preprocess convert example.pdf output_unstructured.md --converter unstructured

# Using MarkItDown
vfn-preprocess convert example.pdf output_markitdown.md --converter markitdown

# Using Docling
vfn-preprocess convert example.pdf output_docling.md --converter docling

# Using Mistral Document AI
vfn-preprocess convert example.pdf output_mistral.md --converter mistral
```

### 2. Compare All Converters

```bash
# This will create an output directory with results from all compatible converters
vfn-preprocess compare example.pdf
```

### 3. Python API Examples

#### Basic Conversion

```python
from pathlib import Path
from vfn_preprocessing import UnstructuredConverter

# For Mistral converter, ensure MISTRAL_API_KEY and MISTRAL_API_URL are set in .env
# from vfn_preprocessing import MistralConverter
# converter = MistralConverter()

converter = UnstructuredConverter()
result = converter.convert(
    input_path=Path('example.pdf'),
    output_path=Path('output.md')
)

print(f"Success: {result['success']}")
print(f"Time: {result['time_seconds']:.2f}s")
```

#### Compare Multiple Converters

```python
from pathlib import Path
from vfn_preprocessing import (
    UnstructuredConverter,
    MarkitdownConverter,
    DoclingConverter,
    MistralConverter
)

input_file = Path('example.pdf')
converters = [
    UnstructuredConverter(),
    MarkitdownConverter(),
    DoclingConverter(),
    MistralConverter()  # Requires MISTRAL_API_KEY and MISTRAL_API_URL in .env
]

results = []
for converter in converters:
    if converter.supports_format(input_file.suffix):
        output_file = Path(f'output_{converter.name.lower()}.md')
        result = converter.convert(input_file, output_file)
        results.append({
            'converter': converter.name,
            'result': result
        })

# Print comparison
for item in results:
    conv = item['converter']
    res = item['result']
    status = '✓' if res['success'] else '✗'
    print(f"{status} {conv}: {res['time_seconds']:.2f}s")
```

#### Custom Processing Logic

```python
from pathlib import Path
from vfn_preprocessing.base import DocumentConverter
from vfn_preprocessing import UnstructuredConverter

def process_document_batch(input_dir: Path, output_dir: Path, converter: DocumentConverter):
    """Process all documents in a directory."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for file_path in input_dir.glob('*'):
        if file_path.is_file() and converter.supports_format(file_path.suffix):
            output_path = output_dir / f"{file_path.stem}.md"
            result = converter.convert(file_path, output_path)
            
            if result['success']:
                print(f"✓ Processed {file_path.name}")
            else:
                print(f"✗ Failed to process {file_path.name}: {result.get('error')}")

# Usage
converter = UnstructuredConverter()
process_document_batch(
    input_dir=Path('documents'),
    output_dir=Path('markdown_output'),
    converter=converter
)
```

## Testing with Different File Types

### PDF Files
```bash
vfn-preprocess compare document.pdf
```

### Word Documents
```bash
vfn-preprocess convert report.docx output.md --converter unstructured
```

### PowerPoint Presentations
```bash
vfn-preprocess convert slides.pptx output.md --converter markitdown
```

### Excel Spreadsheets
```bash
vfn-preprocess convert data.xlsx output.md --converter markitdown
```

## Adding Test Documents

Place your test documents in this directory to experiment with the converters:

```
examples/
├── README.md (this file)
├── sample.pdf
├── document.docx
├── presentation.pptx
└── spreadsheet.xlsx
```

Then run comparisons:

```bash
cd examples
vfn-preprocess compare sample.pdf
```

## Performance Comparison

To compare the performance of different converters, use the `compare` command which will show:
- Execution time for each converter
- Success/failure status
- Output file locations

Example output:
```
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Converter       ┃ Status   ┃ Time (s) ┃ Output File              ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Unstructured.io │ ✓ Success│     2.34 │ sample_unstructured_io.md│
│ MarkItDown      │ ✓ Success│     1.12 │ sample_markitdown.md     │
│ Docling         │ ✓ Success│     3.45 │ sample_docling.md        │
└─────────────────┴──────────┴──────────┴──────────────────────────┘
```

## Tips

1. **Choose the Right Converter**: Different converters excel at different tasks:
   - Use **Unstructured.io** for detailed element extraction and complex documents
   - Use **MarkItDown** for quick conversions and wide format support
   - Use **Docling** for high-quality PDF processing and layout preservation

2. **Batch Processing**: For processing multiple documents, write a simple Python script using the API

3. **Format Support**: Always check format support with `vfn-preprocess list-converters`

4. **Error Handling**: The converters return detailed error information - check the `error` field in failed results
