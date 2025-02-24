from app.models.validators import validate_chunk

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
    assert validated.metadata["filename"] == "test.pdf"