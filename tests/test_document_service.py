# tests/test_document_service.py
import pytest
import os
from app.services.document_service import DocumentService

from pathlib import Path

# This will work from any test file
SAMPLE_DOC_PATH = Path(__file__).parent / "test_data" / "grant_report_with_graph_3_page.pdf"

@pytest.fixture
def document_service():
    return DocumentService()

def test_convert_document(document_service):
    """Test document conversion functionality."""
    if not os.path.exists(SAMPLE_DOC_PATH):
        pytest.skip(f"Sample document not found at {SAMPLE_DOC_PATH}")
    
    # Remove save_intermediate parameter
    result = document_service.convert_document(SAMPLE_DOC_PATH)
    
    # Basic validation
    assert result is not None
    assert hasattr(result, 'document')
    
    # Access the document and check its properties
    doc = result.document
    assert doc is not None
    assert hasattr(doc, 'texts')

def test_process_document_pipeline(document_service):
    """Test the complete document processing pipeline."""
    if not os.path.exists(SAMPLE_DOC_PATH):
        pytest.skip(f"Sample document not found at {SAMPLE_DOC_PATH}")
    
    # Use convert_and_chunk_document instead of convert_chunk_and_embed_document
    chunks = document_service.convert_and_chunk_document(
        SAMPLE_DOC_PATH,
        chunking_strategy="default",
        save_intermediate=False
    )
    
    # Validate results
    assert isinstance(chunks, list)
    assert len(chunks) > 0
    
    # Check structure of processed chunks
    for chunk in chunks:
        # Check dictionary structure instead of attributes
        assert isinstance(chunk, dict)
        assert 'text' in chunk
        assert 'metadata' in chunk
        assert isinstance(chunk['metadata'], dict)
        assert 'chunking_strategy' in chunk['metadata']
        assert 'filename' in chunk['metadata']