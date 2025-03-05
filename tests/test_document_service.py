# tests/test_document_service.py
import pytest
import os
from app.services.document_service import DocumentService

SAMPLE_DOC_PATH = "/home/sng/nanobot-poc/data/sample-pdf-files/grant_decision_email_single_page.pdf"

@pytest.fixture
def document_service():
    return DocumentService()

def test_convert_document(document_service):
    """Test document conversion functionality."""
    if not os.path.exists(SAMPLE_DOC_PATH):
        pytest.skip(f"Sample document not found at {SAMPLE_DOC_PATH}")
    
    # Test with save_intermediate=False to avoid file operations
    result = document_service.convert_document(SAMPLE_DOC_PATH, save_intermediate=False)
    
    # Basic validation
    assert result is not None
    assert hasattr(result, 'document')  # Check if result has a document attribute
    
    # Access the document and check its properties
    doc = result.document
    assert doc is not None
    assert hasattr(doc, 'texts')

def test_process_document_pipeline(document_service):
    """Test the complete document processing pipeline."""
    if not os.path.exists(SAMPLE_DOC_PATH):
        pytest.skip(f"Sample document not found at {SAMPLE_DOC_PATH}")
    
    # Process document with default strategy
    chunks = document_service.process_document(
        SAMPLE_DOC_PATH, 
        chunking_strategy="default",
        save_intermediate=False
    )
    
    # Validate results
    assert isinstance(chunks, list)
    assert len(chunks) > 0
    
    # Check structure of processed chunks
    for chunk in chunks:
        assert "text" in chunk
        assert "metadata" in chunk
        assert "vector" in chunk
        assert len(chunk["vector"]) > 0