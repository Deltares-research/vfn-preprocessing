"""Base class for document converters."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any


class DocumentConverter(ABC):
    """Abstract base class for document converters."""

    def __init__(self, name: str):
        """Initialize the converter with a name.
        
        Args:
            name: Name of the converter implementation
        """
        self.name = name

    @abstractmethod
    def convert(self, input_path: Path, output_path: Path, **kwargs) -> Dict[str, Any]:
        """Convert a document to markdown format.
        
        Args:
            input_path: Path to the input document
            output_path: Path where the markdown output should be saved
            **kwargs: Additional converter-specific options
            
        Returns:
            Dictionary with conversion metadata (time, success, etc.)
        """
        pass

    @abstractmethod
    def supports_format(self, file_extension: str) -> bool:
        """Check if this converter supports the given file format.
        
        Args:
            file_extension: File extension (e.g., '.pdf', '.docx')
            
        Returns:
            True if the format is supported, False otherwise
        """
        pass

    def get_info(self) -> Dict[str, Any]:
        """Get information about this converter.
        
        Returns:
            Dictionary with converter information
        """
        return {
            "name": self.name,
            "class": self.__class__.__name__,
        }
