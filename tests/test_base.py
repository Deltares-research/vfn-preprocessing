"""Tests for base converter class."""

import pytest
from pathlib import Path
from vfn_preprocessing.base import DocumentConverter


class MockConverter(DocumentConverter):
    """Mock converter for testing."""
    
    def __init__(self):
        super().__init__("Mock")
    
    def convert(self, input_path: Path, output_path: Path, **kwargs):
        return {"success": True}
    
    def supports_format(self, file_extension: str) -> bool:
        return file_extension in ['.txt', '.pdf']


def test_converter_initialization():
    """Test converter initialization."""
    converter = MockConverter()
    assert converter.name == "Mock"


def test_converter_get_info():
    """Test get_info method."""
    converter = MockConverter()
    info = converter.get_info()
    assert info["name"] == "Mock"
    assert info["class"] == "MockConverter"


def test_converter_supports_format():
    """Test supports_format method."""
    converter = MockConverter()
    assert converter.supports_format('.txt') is True
    assert converter.supports_format('.pdf') is True
    assert converter.supports_format('.docx') is False
