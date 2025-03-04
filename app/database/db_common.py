"""
Common Database Constants and Utilities

This module provides shared constants, queries, and utility functions
used across all database modules.
"""

import psycopg2
import psycopg2.extras
from app.config.settings import settings

# SQL query to enable the pgvector extension
CREATE_EXTENSION_QUERY = """
CREATE EXTENSION IF NOT EXISTS vector;
"""

# SQL function to validate chunk metadata structure
CREATE_METADATA_CHECK = """
CREATE OR REPLACE FUNCTION validate_chunk_metadata(metadata JSONB)
RETURNS BOOLEAN AS $$
BEGIN
    -- Check if all required fields exist and are of correct type
    IF NOT (
        metadata ? 'filename' AND 
        metadata ? 'page_numbers' AND 
        metadata ? 'title' AND
        metadata ? 'headings' AND
        metadata ? 'chunking_strategy' AND
        jsonb_typeof(metadata->'filename') = 'string' AND
        jsonb_typeof(metadata->'title') = 'string' AND
        jsonb_typeof(metadata->'page_numbers') = 'array' AND
        jsonb_typeof(metadata->'headings') = 'array' AND
        jsonb_typeof(metadata->'chunking_strategy') = 'string'
    ) THEN
        RETURN FALSE;
    END IF;
    
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;
"""

# SQL query to create the chunks table with vector support and metadata validation
CREATE_TABLE_QUERY = f"""
CREATE TABLE IF NOT EXISTS chunks (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    vector VECTOR({settings.openai.embedding_dimensions}) NOT NULL,
    metadata JSONB NOT NULL,
    CONSTRAINT valid_metadata CHECK (validate_chunk_metadata(metadata))
);
"""

# SQL query to insert a new chunk
INSERT_CHUNK_QUERY = """
    INSERT INTO chunks (text, vector, metadata)
    VALUES (%s, %s, %s)
    RETURNING id;
"""

def get_connection() -> psycopg2.connect: 
    """Connect to the PostgreSQL database using settings configuration."""
    try:
        return psycopg2.connect(**settings.local_db.get_connection_dict())
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise 