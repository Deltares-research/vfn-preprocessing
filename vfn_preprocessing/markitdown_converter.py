"""MarkItDown document converter."""

import time
from pathlib import Path
from typing import Dict, Any

from vfn_preprocessing.base import DocumentConverter


class MarkitdownConverter(DocumentConverter):
    """Document converter using MarkItDown library."""

    def __init__(self):
        """Initialize the MarkItDown converter."""
        super().__init__("MarkItDown")
        self._supported_formats = {
            '.pdf', '.docx', '.pptx', '.xlsx',
            '.jpg', '.jpeg', '.png', '.gif',
            '.html', '.htm', '.txt', '.csv',
            '.json', '.xml', '.zip', '.wav', '.mp3'
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
        """Convert a document to markdown using MarkItDown.
        
        Args:
            input_path: Path to the input document
            output_path: Path where the markdown output should be saved
            **kwargs: Additional options
            
        Returns:
            Dictionary with conversion metadata
        """
        from markitdown import MarkItDown
        
        start_time = time.time()
        
        try:
            # Initialize MarkItDown
            md = MarkItDown()
            
            # Convert the document
            result = md.convert(str(input_path))
            
            # Write to output file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(result.text_content, encoding='utf-8')
            
            elapsed_time = time.time() - start_time
            
            return {
                "success": True,
                "converter": self.name,
                "time_seconds": elapsed_time,
                "output_path": str(output_path)
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
