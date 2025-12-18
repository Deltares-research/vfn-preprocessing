"""Mistral document converter."""

import base64
import json
import os
import time
from pathlib import Path
from typing import Dict, Any, List

from dotenv import load_dotenv
import requests
from PyPDF2 import PdfReader, PdfWriter

from vfn_preprocessing.base import DocumentConverter

bbox_annotation_format = {
  "type": "json_schema",
  "json_schema": {
    "schema": {
      "properties": {
        "document_type": {
          "title": "Document_Type",
          "description": "The type of the image.",
          "type": "string"
        },
        "summary": {
          "title": "Summary",
          "description": "Summarize the image.",
          "type": "string"
        }
      },
      "required": [
        "document_type",
        "summary"
      ],
      "title": "BBOXAnnotation",
      "type": "object",
      "additionalProperties": False
    },
    "name": "document_annotation",
    "strict": True
  }
}

class MistralConverter(DocumentConverter):
    """Document converter using Mistral Document AI API."""

    def __init__(self):
        """Initialize the Mistral converter.
        
        Args:
            api_key: Mistral API key. If not provided, will read from MISTRAL_API_KEY env var.
            api_url: Mistral API endpoint URL. Defaults to Azure endpoint.
        """
        super().__init__("Mistral")
        load_dotenv()
        self.api_key = os.getenv("MISTRAL_API_KEY", "")
        self.api_url = os.getenv("MISTRAL_API_URL", "")
        self._supported_formats = {'.pdf', '.jpg', '.jpeg', '.png', '.docx', '.xlsx', '.pptx'}
        
        if not self.api_key:
            raise ValueError("Mistral API key must be set in MISTRAL_API_KEY environment variable")
        if not self.api_url:
            raise ValueError("Mistral API URL must be set in MISTRAL_API_URL environment variable")

    def supports_format(self, file_extension: str) -> bool:
        """Check if this converter supports the given file format.
        
        Args:
            file_extension: File extension (e.g., '.pdf')
            
        Returns:
            True if the format is supported, False otherwise
        """
        return file_extension.lower() in self._supported_formats

    def _split_pdf(self, input_path: Path, max_pages: int = 30) -> List[bytes]:
        """Split a PDF into chunks of max_pages.
        
        Args:
            input_path: Path to the PDF file
            max_pages: Maximum pages per chunk
            
        Returns:
            List of PDF chunks as bytes
        """        
        reader = PdfReader(str(input_path))
        total_pages = len(reader.pages)
        chunks = []
        
        for start_page in range(0, total_pages, max_pages):
            end_page = min(start_page + max_pages, total_pages)
            writer = PdfWriter()
            
            for page_num in range(start_page, end_page):
                writer.add_page(reader.pages[page_num])
            
            # Write chunk to bytes
            from io import BytesIO
            chunk_bytes = BytesIO()
            writer.write(chunk_bytes)
            chunks.append(chunk_bytes.getvalue())
        
        return chunks
    
    def _convert_chunk(self, chunk_data: bytes, mime_type: str, model: str, include_image_base64: bool) -> str:
        """Convert a single document chunk to markdown.
        
        Args:
            chunk_data: Document data as bytes
            mime_type: MIME type of the document
            model: Model name to use
            include_image_base64: Whether to include images as base64
            
        Returns:
            Markdown text from the chunk
        """
        encoded_chunk = base64.b64encode(chunk_data).decode('utf-8')
        
        payload = json.dumps({
            "model": model,
            "document": {
                "type": "document_url",
                "document_url": f"data:{mime_type};base64,{encoded_chunk}"
            },
            "bbox_annotation_format": bbox_annotation_format,
            "include_image_base64": include_image_base64
        })
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

        response = requests.post(self.api_url, headers=headers, data=payload)
        response.raise_for_status()
        
        response_data = response.json()
        text_output = ""
        for page in response_data.get("pages", []):
            text_output += page.get("markdown", "")
            text_output += "\n\n"
            images = page.get("images", [])
            for img in images:
                #TODO: check document type and include accordingly (only charts or diagrams for example)
                text_output += json.loads(img.get("image_annotation", "")).get("summary", "")
                text_output += "\n\n"
        return text_output

    def convert(self, input_path: Path, output_path: Path, **kwargs) -> Dict[str, Any]:
        """Convert a document to markdown using Mistral Document AI.
        
        Args:
            input_path: Path to the input document
            output_path: Path where the markdown output should be saved
            **kwargs: Additional options:
                - model: Model name (default: "mistral-document-ai-2505")
                - include_image_base64: Whether to include images as base64 (default: True)
                - max_pages: Maximum pages per API request for PDFs (default: 30)
            
        Returns:
            Dictionary with conversion metadata
        """
        start_time = time.time()
        
        try:
            # Determine MIME type based on file extension
            file_extension = input_path.suffix.lower()
            mime_type_map = {
                '.pdf': 'application/pdf',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
            }
            mime_type = mime_type_map.get(file_extension, 'application/pdf')
            
            # Prepare API request parameters
            model = kwargs.get("model", "mistral-document-ai-2505")
            include_image_base64 = kwargs.get("include_image_base64", True)
            max_pages = kwargs.get("max_pages", 30)
            
            text_output = ""
            total_pages = 0
            
            # Check if PDF needs splitting
            if file_extension == '.pdf':
                reader = PdfReader(str(input_path))
                total_pages = len(reader.pages)
                
                if total_pages > max_pages:
                    # Split and process in chunks
                    chunks = self._split_pdf(input_path, max_pages)
                    
                    for i, chunk_data in enumerate(chunks):
                        chunk_text = self._convert_chunk(chunk_data, mime_type, model, include_image_base64)
                        text_output += chunk_text
                        if i < len(chunks) - 1:
                            text_output += "\n\n"  # Add spacing between chunks
                else:
                    # Single request for small PDFs
                    with open(input_path, "rb") as file:
                        chunk_data = file.read()
                    text_output = self._convert_chunk(chunk_data, mime_type, model, include_image_base64)
            else:
                # Non-PDF - single request
                with open(input_path, "rb") as file:
                    chunk_data = file.read()
                text_output = self._convert_chunk(chunk_data, mime_type, model, include_image_base64)
            
            # Write output to file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text_output)
            
            conversion_time = time.time() - start_time
            
            return {
                "success": True,
                "converter": self.name,
                "input_path": str(input_path),
                "output_path": str(output_path),
                "time_seconds": conversion_time,
                "num_pages": total_pages if total_pages > 0 else "unknown",
                "model": model
            }
            
        except requests.exceptions.RequestException as e:
            conversion_time = time.time() - start_time
            return {
                "success": False,
                "converter": self.name,
                "input_path": str(input_path),
                "output_path": str(output_path),
                "time_seconds": conversion_time,
                "error": f"API request failed: {str(e)}"
            }
        except Exception as e:
            conversion_time = time.time() - start_time
            return {
                "success": False,
                "converter": self.name,
                "input_path": str(input_path),
                "output_path": str(output_path),
                "time_seconds": conversion_time,
                "error": str(e)
            }
