"""Tests for converter implementations."""

import pytest
from pathlib import Path
from vfn_preprocessing import (
    UnstructuredConverter,
    MarkitdownConverter,
    DoclingConverter,
)


def test_unstructured_converter_initialization():
    """Test Unstructured converter initialization."""
    converter = UnstructuredConverter()
    assert converter.name == "Unstructured.io"
    assert converter.supports_format('.pdf')
    assert converter.supports_format('.docx')


def test_markitdown_converter_initialization():
    """Test MarkItDown converter initialization."""
    converter = MarkitdownConverter()
    assert converter.name == "MarkItDown"
    assert converter.supports_format('.pdf')
    assert converter.supports_format('.xlsx')


def test_docling_converter_initialization():
    """Test Docling converter initialization."""
    converter = DoclingConverter()
    assert converter.name == "Docling"
    assert converter.supports_format('.pdf')
    assert converter.supports_format('.docx')


def test_converter_unsupported_format():
    """Test that converters correctly identify unsupported formats."""
    converter = UnstructuredConverter()
    assert not converter.supports_format('.xyz')
    
    converter = MarkitdownConverter()
    assert not converter.supports_format('.unknown')
    
    converter = DoclingConverter()
    assert not converter.supports_format('.fake')
