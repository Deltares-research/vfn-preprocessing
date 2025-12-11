"""Tests for converter implementations."""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch
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


def test_unstructured_formula_handling(tmp_path):
    """Test that Formula elements are converted to LaTeX markdown format."""
    converter = UnstructuredConverter()
    
    # Create mock elements with different types including Formula
    mock_elements = [
        Mock(category="Title", text="Test Document"),
        Mock(category="NarrativeText", text="This is a test."),
        Mock(category="Formula", text="E = mc^2"),
        Mock(category="Formula", text="\\int_{0}^{\\infty} e^{-x^2} dx = \\frac{\\sqrt{\\pi}}{2}"),
    ]
    
    input_path = tmp_path / "test.txt"
    output_path = tmp_path / "output.md"
    input_path.write_text("Test content")
    
    # Mock the partition function to return our mock elements
    with patch('unstructured.partition.auto.partition', return_value=mock_elements):
        result = converter.convert(input_path, output_path)
    
    assert result["success"] is True
    
    # Check the output content
    output_content = output_path.read_text()
    
    # Check that short formulas are inline
    assert "$E = mc^2$" in output_content
    
    # Check that longer formulas are in display math mode
    assert "$$\n" in output_content
    assert "\\int_{0}^{\\infty}" in output_content


def test_unstructured_table_handling(tmp_path):
    """Test that Table elements with HTML metadata are converted to Markdown tables."""
    converter = UnstructuredConverter()
    
    # Create mock table element with HTML metadata
    html_table = """
    <table>
        <tr><th>Name</th><th>Age</th><th>City</th></tr>
        <tr><td>Alice</td><td>30</td><td>New York</td></tr>
        <tr><td>Bob</td><td>25</td><td>London</td></tr>
    </table>
    """
    
    mock_metadata = Mock()
    mock_metadata.text_as_html = html_table
    
    table_element = Mock(category="Table", text="Name Age City Alice 30 New York Bob 25 London")
    table_element.metadata = mock_metadata
    
    mock_elements = [
        Mock(category="Title", text="Test Table"),
        table_element,
    ]
    
    input_path = tmp_path / "test.txt"
    output_path = tmp_path / "output.md"
    input_path.write_text("Test content")
    
    # Mock the partition function to return our mock elements
    with patch('unstructured.partition.auto.partition', return_value=mock_elements):
        result = converter.convert(input_path, output_path)
    
    assert result["success"] is True
    
    # Check the output content
    output_content = output_path.read_text()
    
    # Check that the table is in Markdown format
    assert "| Name | Age | City |" in output_content
    assert "| --- |" in output_content
    assert "| Alice | 30 | New York |" in output_content
    assert "| Bob | 25 | London |" in output_content

