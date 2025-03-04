"""
Database Insertion Operations

This module provides functions for inserting data into the database,
including single chunk insertion and bulk operations.
"""

import json
from app.database.db_common import INSERT_CHUNK_QUERY
from app.models.validators import validate_chunk

def insert_chunk(conn, text, vector, metadata) -> int:
    """Insert a new chunk into the database.
    
    Args:
        conn: Database connection
        text: Chunk text content
        vector: Embedding vector (3072 dimensions)
        metadata: Metadata as dictionary, Pydantic model, or JSON string
        
    Returns:
        The ID of the inserted chunk
        
    Raises:
        ValueError: If vector is None
    """
    # Validate that vector is provided
    if vector is None:
        raise ValueError("Vector cannot be None")
    
    # Serialize metadata if it's not already a string
    if not isinstance(metadata, str):
        # Handle Pydantic models
        if hasattr(metadata, 'model_dump'):  # Pydantic v2
            metadata = metadata.model_dump()
        elif hasattr(metadata, 'dict'):  # Pydantic v1
            metadata = metadata.dict()
            
        metadata = json.dumps(metadata)
        
    with conn.cursor() as cur:
        cur.execute(INSERT_CHUNK_QUERY, (text, vector, metadata))
        chunk_id = cur.fetchone()[0]
        print(f"✅ Inserted chunk with id: {chunk_id}")
        return chunk_id

def bulk_validate_and_insert_chunks(conn, chunks: list[dict]) -> list[int]:
    """Validate and insert multiple chunks in a single transaction.
    
    Args:
        conn: Database connection
        chunks: List of dictionaries containing text, vector, and metadata
        
    Returns:
        List of inserted chunk IDs
        
    Raises:
        Exception: If validation or insertion fails
    """
    chunk_ids = []
    
    try:
        with conn.cursor() as cur:
            for chunk in chunks:
                # Validate each chunk using the Pydantic model
                validated_chunk = validate_chunk(chunk)
                
                # Convert Pydantic model to dictionary before JSON serialization
                metadata_dict = validated_chunk.metadata.model_dump()
                
                cur.execute(INSERT_CHUNK_QUERY, (
                    validated_chunk.text,
                    validated_chunk.vector,
                    json.dumps(metadata_dict)
                ))
                chunk_id = cur.fetchone()[0]
                chunk_ids.append(chunk_id)
            
        # Commit the transaction after all chunks are inserted
        conn.commit()
        print(f"✅ Successfully processed {len(chunk_ids)} chunks")
        return chunk_ids
        
    except Exception as e:
        # Rollback the transaction if any error occurs
        print(f"❌ Error in bulk processing: {e}")
        conn.rollback()
        raise 