"""Docling document converter."""

import time
from pathlib import Path
from typing import Dict, Any

from vfn_preprocessing.base import DocumentConverter


class DoclingConverter(DocumentConverter):
    """Document converter using Docling library."""

    def __init__(self):
        """Initialize the Docling converter."""
        super().__init__("Docling")
        self._supported_formats = {
            '.pdf', '.docx', '.pptx', '.html',
            '.asciidoc', '.md', '.markdown'
        }

    def supports_format(self, file_extension: str) -> bool:
        """Check if this converter supports the given file format.
        
        Args:
            file_extension: File extension (e.g., '.pdf', '.docx')
            
        Returns:
            True if the format is supported, False otherwise
        """
        return file_extension.lower() in self._supported_formats

    def convert(self, input_path: Path, output_path: Path, **kwargs) -> Dict[str, Any]:
        """Convert a document to markdown using Docling.
        
        Args:
            input_path: Path to the input document
            output_path: Path where the markdown output should be saved
            **kwargs: Additional options
            
        Returns:
            Dictionary with conversion metadata
        """
        from docling.document_converter import DocumentConverter
        
        start_time = time.time()
        
        try:
            # Initialize Docling converter
            converter = DocumentConverter()
            
            # Convert the document
            result = converter.convert(str(input_path))
            
            # Export to markdown
            markdown_content = result.document.export_to_markdown()
            
            # Write to output file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(markdown_content, encoding='utf-8')
            
            elapsed_time = time.time() - start_time
            
            return {
                "success": True,
                "converter": self.name,
                "time_seconds": elapsed_time,
                "output_path": str(output_path),
                "pages": len(result.document.pages) if hasattr(result.document, 'pages') else None
            }
            
        except Exception as e:
            elapsed_time = time.time() - start_time
            return {
                "success": False,
                "converter": self.name,
                "time_seconds": elapsed_time,
                "error": str(e),
                "output_path": str(output_path)
            }
