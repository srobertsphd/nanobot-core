from .db_schemas import ChunkMetadata, Chunks
from pydantic import ValidationError

def validate_chunk_metadata(metadata: dict) -> ChunkMetadata:
    """
    Validate chunk metadata using Pydantic model.
    
    Args:
        metadata (dict): Metadata dictionary to validate
        
    Returns:
        ChunkMetadata: Validated metadata model
        
    Raises:
        ValidationError: If metadata is invalid
    """
    if not metadata:
        raise ValueError("Metadata is required")
    return ChunkMetadata(**metadata)

def validate_chunk(text: str, vector: list, metadata_id: int) -> Chunks:
    """
    Validate chunk data using Pydantic model.
    
    Args:
        text (str): Chunk text
        vector (list): Embedding vector
        metadata_id (int): Associated metadata ID
        
    Returns:
        Chunks: Validated chunk model
        
    Raises:
        ValidationError: If chunk data is invalid
    """
    return Chunks(
        text=text,
        vector=vector,
        metadata_id=metadata_id
    )