"""Unstructured.io document converter."""

import os
import time
from pathlib import Path
from typing import Dict, Any

from dotenv import load_dotenv

from vfn_preprocessing.base import DocumentConverter


def _html_table_to_markdown(html: str) -> str:
    """Convert an HTML table to Markdown format.
    
    Args:
        html: HTML table string
        
    Returns:
        Markdown formatted table
    """
    try:
        from html.parser import HTMLParser
        
        class TableParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.rows = []
                self.current_row = []
                self.current_cell = []
                self.in_table = False
                self.in_row = False
                self.in_cell = False
                
            def handle_starttag(self, tag, attrs):
                if tag == 'table':
                    self.in_table = True
                elif tag == 'tr':
                    self.in_row = True
                    self.current_row = []
                elif tag in ('td', 'th'):
                    self.in_cell = True
                    self.current_cell = []
                    
            def handle_endtag(self, tag):
                if tag == 'table':
                    self.in_table = False
                elif tag == 'tr':
                    self.in_row = False
                    if self.current_row:
                        self.rows.append(self.current_row)
                elif tag in ('td', 'th'):
                    self.in_cell = False
                    cell_text = ''.join(self.current_cell).strip()
                    self.current_row.append(cell_text)
                    
            def handle_data(self, data):
                if self.in_cell:
                    self.current_cell.append(data)
        
        parser = TableParser()
        parser.feed(html)
        
        if not parser.rows:
            return html
        
        # Build markdown table
        markdown_lines = []
        
        for i, row in enumerate(parser.rows):
            # Escape pipe characters in cells
            escaped_row = [cell.replace('|', '\\|') for cell in row]
            markdown_lines.append('| ' + ' | '.join(escaped_row) + ' |')
            
            # Add header separator after first row
            if i == 0:
                separator = '|' + '|'.join([' --- ' for _ in row]) + '|'
                markdown_lines.append(separator)
        
        return '\n'.join(markdown_lines)
        
    except Exception:
        # Fallback to original HTML if parsing fails
        return html


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
            
        Note:
            - Formula elements are automatically converted to LaTeX format:
              * Short formulas (<50 chars, single-line) use inline math: $formula$
              * Longer/multi-line formulas use display math: $$\\nformula\\n$$
            - Table elements use metadata.text_as_html when available and are
              converted to proper Markdown table format
        """
        import unstructured_client
        from unstructured_client.models import shared
        
        start_time = time.time()
        
        try:
            # Partition the document using open source
            # from unstructured.partition.auto import partition
            # elements = partition(str(input_path))

            # Initialize client with API key from environment
            load_dotenv()
            api_key = os.getenv("UNSTRUCTURED_API_KEY")
            if not api_key:
                print("Warning: UNSTRUCTURED_API_KEY not found in environment")
                return {"success": False, "error": "Missing UNSTRUCTURED_API_KEY"}
            
            client = unstructured_client.UnstructuredClient(
                api_key_auth=api_key
            )

            # Build request following the SDK documentation pattern
            req = {
                "partition_parameters": {
                    "files": {
                        "content": open(input_path, "rb"),
                        "file_name": os.path.basename(input_path),
                    },
                    "chunking_strategy": "by_title",
                    # "max_characters": 1024,
                    "strategy": shared.Strategy.VLM,
                    "vlm_model": "gpt-4o",
                    "vlm_model_provider": "openai",
                    "split_pdf_page": False,
                    "split_pdf_allow_failed": True,
                    "split_pdf_concurrency_level": 15
                }
            }
            
            # Make synchronous API call
            res = client.general.partition(request=req)
            elements = res.elements or []
            
            # Convert elements to markdown
            markdown_content = []
            for element in elements:
                element_type = element["type"]
                text = element["text"]
                
                # Format based on element type
                if element_type == "Title":
                    markdown_content.append(f"# {text}")
                elif element_type == "NarrativeText":
                    markdown_content.append(text)
                elif element_type == "ListItem":
                    markdown_content.append(f"- {text}")
                elif element_type == "Table":
                    # Use HTML table from metadata if available for better formatting
                    if "metadata" in element and "text_as_html" in element["metadata"]:
                        html_table = element["metadata"]["text_as_html"]
                        if html_table:
                            markdown_table = _html_table_to_markdown(html_table)
                            markdown_content.append(markdown_table)
                        else:
                            markdown_content.append(text)
                    else:
                        markdown_content.append(text)
                elif element_type == "Formula":
                    # Format formulas as inline or block LaTeX depending on length/complexity
                    formula_text = text.strip()
                    if formula_text:
                        # Use inline math for short formulas, display math for longer ones
                        if len(formula_text) < 50 and '\n' not in formula_text:
                            markdown_content.append(f"${formula_text}$")
                        else:
                            markdown_content.append(f"$$\n{formula_text}\n$$")
                elif (element_type == "Header" or element_type == "Footer" or element_type == "PageBreak" or element_type == "PageNumber"):
                    # Skip these elements
                    continue
                else:
                    markdown_content.append(text)
            
            # Write to output file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text("\n\n".join(markdown_content), encoding='utf-8')
            
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
