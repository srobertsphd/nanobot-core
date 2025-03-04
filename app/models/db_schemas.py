"""
Database Schema Models

This module defines Pydantic models that represent the structure of data
stored in the database. These models are used for validation and type checking
when inserting or retrieving data.
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import List
from app.config.settings import settings


class ChunkMetadata(BaseModel):
    """
    Metadata associated with a text chunk.
    
    Contains information about the source document and location.
    """
    filename: str  # Source document filename
    title: str     # Document title
    page_numbers: List[int]  # Page numbers where this chunk appears
    headings: List[str]  # Hierarchical headings associated with this chunk
    chunking_strategy: str  # Strategy used for chunking (default, balanced, fine_grained, etc.)
    # Add any other optional fields you might want to include
    

class Chunks(BaseModel):
    """
    Represents a text chunk with its embedding vector and metadata.
    
    This is the main data structure stored in the database.
    """
    text: str  # The actual text content
    vector: List[float] = Field(
        min_length=settings.openai.embedding_dimensions, 
        max_length=settings.openai.embedding_dimensions
    )  # Embedding vector (fixed dimension)
    metadata: ChunkMetadata  # Associated metadata
    
    model_config = ConfigDict(  # New style Pydantic v2 config
        arbitrary_types_allowed=True
    )
