"""
Common Database Constants and Utilities

This module provides shared constants, queries, and utility functions
used across all database modules.
"""

import psycopg2
import psycopg2.extras
from app.config.settings import settings

# # SQL query to enable the pgvector extension
# CREATE_EXTENSION_QUERY = """
# CREATE EXTENSION IF NOT EXISTS vector;
# """

# # SQL function to validate chunk metadata structure
# CREATE_METADATA_CHECK = """
# CREATE OR REPLACE FUNCTION validate_chunk_metadata(metadata JSONB)
# RETURNS BOOLEAN AS $$
# BEGIN
#     -- Check if all required fields exist and are of correct type
#     IF NOT (
#         metadata ? 'filename' AND 
#         metadata ? 'page_numbers' AND 
#         metadata ? 'title' AND
#         metadata ? 'headings' AND
#         metadata ? 'chunking_strategy' AND
#         jsonb_typeof(metadata->'filename') = 'string' AND
#         jsonb_typeof(metadata->'title') = 'string' AND
#         jsonb_typeof(metadata->'page_numbers') = 'array' AND
#         jsonb_typeof(metadata->'headings') = 'array' AND
#         jsonb_typeof(metadata->'chunking_strategy') = 'string'
#     ) THEN
#         RETURN FALSE;
#     END IF;
    
#     RETURN TRUE;
# END;
# $$ LANGUAGE plpgsql;
# """

# # SQL query to create the chunks table with vector support and metadata validation
# CREATE_TABLE_QUERY = f"""
# CREATE TABLE IF NOT EXISTS chunks (
#     id SERIAL PRIMARY KEY,
#     text TEXT NOT NULL,
#     vector VECTOR({settings.openai.embedding_dimensions}) NOT NULL,
#     metadata JSONB NOT NULL,
#     CONSTRAINT valid_metadata CHECK (validate_chunk_metadata(metadata))
# );
# """

# # SQL query to insert a new chunk
# INSERT_CHUNK_QUERY = """
#     INSERT INTO chunks (text, vector, metadata)
#     VALUES (%s, %s, %s)
#     RETURNING id;
# """

def get_connection(use_neon=None) -> psycopg2.connect:
    """
    Connect to the PostgreSQL database using settings configuration.
    gives the option to override the settings.use_neon flag
    
    Args:
        use_neon (bool, optional): Override settings.use_neon flag.
            If None, uses the value from settings.use_neon.
    
    Returns:
        psycopg2.connect: Database connection
        
    Raises:
        psycopg2.Error: If connection fails
    """
    try:
        # Determine whether to use Neon
        if use_neon is None:
            use_neon = settings.use_neon
            
        if use_neon:
            # Connect to Neon using URL
            conn = psycopg2.connect(settings.neon_db.db_url)
            print("Connected to Neon database")
        else:
            # Connect to local database using connection parameters
            conn = psycopg2.connect(**settings.local_db.get_connection_dict())
            print("Connected to local database")
            
        return conn
    except psycopg2.Error as e:
        db_type = "Neon" if use_neon else "local"
        print(f"Error connecting to {db_type} database: {e}")
        raise 