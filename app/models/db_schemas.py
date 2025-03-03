"""
Database Schema Models

This module defines Pydantic models that represent the structure of data
stored in the database. These models are used for validation and type checking
when inserting or retrieving data.
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional


class ChunkMetadata(BaseModel):
    """
    Metadata associated with a text chunk.
    
    Contains information about the source document and location.
    """
    filename: str  # Source document filename
    title: str     # Document title
    page_numbers: List[int]  # Page numbers where this chunk appears
    headings: Optional[List[str]] = None  # remove optional and none when rebuilding db
    chunking_strategy: Optional[str] = "default"  # remove optional anddefault when rebuilding db
    # Add any other optional fields you might want to include
    

class Chunks(BaseModel):
    """
    Represents a text chunk with its embedding vector and metadata.
    
    This is the main data structure stored in the database.
    """
    text: str  # The actual text content
    vector: List[float] = Field(min_length=3072, max_length=3072)  # Embedding vector (fixed dimension)
    metadata: ChunkMetadata  # Associated metadata
    
    model_config = ConfigDict(  # New style Pydantic v2 config
        arbitrary_types_allowed=True
    )
