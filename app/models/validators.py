from .db_schemas import Chunks
from pydantic import ValidationError

def validate_chunk(chunk_data: dict) -> Chunks:
    """
    Validate chunk data with flexible metadata structure.
    
    Args:
        chunk_data (dict): Dictionary containing text, vector, and metadata
        
    Returns:
        Chunks: Validated chunk model
        
    Raises:
        ValidationError: If data is invalid
    """
    if not chunk_data:
        raise ValueError("Chunk data is required")
    
    if "metadata" not in chunk_data or not isinstance(chunk_data["metadata"], dict):
        raise ValueError("Metadata must be a dictionary")
    
    validated = Chunks(**chunk_data)
    
    print("✅ Chunk validation successful:")
    print(f"  • Text length: {len(validated.text)} chars")
    print(f"  • Vector dimensions: {len(validated.vector)}")
    print(f"  • Metadata fields: {list(validated.metadata.keys())}")
    
    return validated