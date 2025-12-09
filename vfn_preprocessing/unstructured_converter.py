"""Unstructured.io document converter."""

import time
from pathlib import Path
from typing import Dict, Any

from vfn_preprocessing.base import DocumentConverter


class UnstructuredConverter(DocumentConverter):
    """Document converter using Unstructured.io library."""

    def __init__(self):
        """Initialize the Unstructured converter."""
        super().__init__("Unstructured.io")
        self._supported_formats = {
            '.pdf', '.docx', '.doc', '.pptx', '.ppt', 
            '.xlsx', '.xls', '.html', '.xml', '.txt',
            '.eml', '.msg', '.rtf', '.odt', '.epub'
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
        """Convert a document to markdown using Unstructured.
        
        Args:
            input_path: Path to the input document
            output_path: Path where the markdown output should be saved
            **kwargs: Additional options (e.g., strategy='hi_res', mode='elements')
            
        Returns:
            Dictionary with conversion metadata
        """
        from unstructured.partition.auto import partition
        
        start_time = time.time()
        
        try:
            # Partition the document
            elements = partition(str(input_path))
            
            # Convert elements to markdown
            markdown_content = []
            for element in elements:
                element_type = element.category
                text = element.text
                
                # Format based on element type
                if element_type == "Title":
                    markdown_content.append(f"# {text}\n")
                elif element_type == "NarrativeText":
                    markdown_content.append(f"{text}\n")
                elif element_type == "ListItem":
                    markdown_content.append(f"- {text}\n")
                elif element_type == "Table":
                    markdown_content.append(f"{text}\n")
                else:
                    markdown_content.append(f"{text}\n")
            
            # Write to output file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text("\n".join(markdown_content), encoding='utf-8')
            
            elapsed_time = time.time() - start_time
            
            return {
                "success": True,
                "converter": self.name,
                "time_seconds": elapsed_time,
                "elements_count": len(elements),
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
