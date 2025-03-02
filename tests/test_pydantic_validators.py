from app.models.validators import validate_chunk
import pytest
from pydantic import ValidationError

def test_validate_chunk_basic():
    """Test basic validation of a well-formed chunk"""
    test_chunk = {
        "text": "This is a test chunk",
        "vector": [0.1] * 3072,  # Creates list of 3072 elements
        "metadata": {
            "filename": "test.pdf",
            "page_numbers": [1],
            "title": "Test Document"
        }
    }
    
    validated = validate_chunk(test_chunk)
    assert validated.text == test_chunk["text"]
    assert len(validated.vector) == 3072
    
    # Access metadata fields directly from the ChunkMetadata object
    assert validated.metadata.filename == test_chunk["metadata"]["filename"]
    assert validated.metadata.page_numbers == test_chunk["metadata"]["page_numbers"]
    assert validated.metadata.title == test_chunk["metadata"]["title"]


def test_validate_chunk_missing_metadata_field():
    """Test validation fails when metadata is missing required fields"""
    test_chunk = {
        "text": "This is a test chunk",
        "vector": [0.1] * 3072,
        "metadata": {
            "filename": "test.pdf",
            # Missing "page_numbers"
            "title": "Test Document"
        }
    }
    
    # This should raise a validation error
    with pytest.raises(ValidationError):
        validate_chunk(test_chunk)

def test_validate_chunk_wrong_vector_length():
    """Test validation fails when vector has wrong length"""
    test_chunk = {
        "text": "This is a test chunk",
        "vector": [0.1] * 3000,  # Wrong length (3000 instead of 3072)
        "metadata": {
            "filename": "test.pdf",
            "page_numbers": [1],
            "title": "Test Document"
        }
    }
    
    # This should raise a validation error
    with pytest.raises(ValidationError):
        validate_chunk(test_chunk)