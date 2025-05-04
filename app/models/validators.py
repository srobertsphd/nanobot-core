"""
Data Validation Functions

This module provides functions for validating data structures before
they are processed or stored in the database.
"""

from .models import Chunks


def validate_chunk(chunk_data: dict) -> Chunks:
    """
    Validate chunk data with flexible metadata structure.
    
    Args:
        chunk_data (dict): Dictionary containing text, vector, and metadata
        
    Returns:
        Chunks: Validated chunk model
    """
    if not chunk_data:
        raise ValueError("Chunk data is required")
    
    if "metadata" not in chunk_data or not isinstance(chunk_data["metadata"], dict):
        raise ValueError("Metadata must be a dictionary")
    
    validated = Chunks(**chunk_data)
    
    print("✅ Chunk validation successful:")
    print(f"  • Text length: {len(validated.text)} chars")
    print(f"  • Vector dimensions: {len(validated.vector)}")
    
    # Get metadata field names from the Pydantic model
    metadata_fields = validated.metadata.model_dump().keys() 
    
    print(f"  • Metadata fields: {list(metadata_fields)}")
    
    return validated