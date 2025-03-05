import pytest
from app.services.document_service import DocumentService
from app.database.db_insert import bulk_validate_and_insert_chunks
from app.database.db_common import get_connection
from app.models.validators import validate_chunk

@pytest.fixture
def db_connection():
    """Provide a database connection for tests."""
    conn = get_connection()
    
    # Make sure we're using transactions for tests
    conn.autocommit = False
    
    # Yield the connection to the test
    yield conn
    
    # After the test, roll back any changes to keep the database clean
    conn.rollback()
    
    # Close the connection
    conn.close()

def test_document_service_invalid_path():
    """Test DocumentService with invalid file path."""
    service = DocumentService()
    
    with pytest.raises(FileNotFoundError):
        service.convert_document("nonexistent_file.pdf")

def test_validate_chunk_invalid_data():
    """Test chunk validation with invalid data."""
    # Test with missing text
    with pytest.raises(ValueError):
        validate_chunk({"vector": [0.1] * 1536, "metadata": {"filename": "test.pdf"}})
    
    # Test with invalid vector length
    with pytest.raises(Exception):
        validate_chunk({
            "text": "Test",
            "vector": [0.1] * 100,  # Wrong length
            "metadata": {
                "filename": "test.pdf",
                "page_numbers": [1],
                "title": "Test",
                "headings": ["Test"],
                "chunking_strategy": "default"
            }
        })

def test_bulk_insert_empty_list(db_connection):
    """Test bulk insert with empty list."""
    result = bulk_validate_and_insert_chunks(db_connection, [])
    assert result == []
