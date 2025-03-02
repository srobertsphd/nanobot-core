"""
PostgreSQL Database Interface with pgvector Support

This module provides functions for interacting with a PostgreSQL database
that uses the pgvector extension for vector similarity search. It handles
database connection, table creation, and vector-based operations.
"""

import psycopg2
import json
from app.utils.openai_embedding import get_embedding
from app.models.validators import validate_chunk
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
        jsonb_typeof(metadata->'filename') = 'string' AND
        jsonb_typeof(metadata->'title') = 'string' AND
        jsonb_typeof(metadata->'page_numbers') = 'array'
    ) THEN
        RETURN FALSE;
    END IF;
    
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;
"""

# SQL query to create the chunks table with vector support and metadata validation
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS chunks (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    vector VECTOR(3072) NOT NULL,
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

def get_connection():
    """
    Establish a connection to the PostgreSQL database.
    
    Returns:
        psycopg2.connection: A connection object to the database
        
    Raises:
        psycopg2.Error: If connection fails
    """
    try:
        return psycopg2.connect(**settings.local_db.get_connection_dict())
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def create_database(db_name):
    """
    Create a new PostgreSQL database.
    
    Args:
        db_name (str): Name of the database to create
        
    Note:
        This function uses admin credentials from settings
    """
    # Use admin login information for database creation
    conn = psycopg2.connect(**settings.admin_db.get_connection_dict())
    conn.autocommit = True  
    cur = conn.cursor()

    try:
        cur.execute(f"CREATE DATABASE {db_name}")
        print(f"Database {db_name} created successfully")
    except psycopg2.Error as e:
        print(f"Error creating database: {e}")
    finally:
        cur.close()
        conn.close()


def enable_pgvector_extension(conn):
    """
    Enable the pgvector extension in the PostgreSQL database.
    
    Args:
        conn (psycopg2.connection): Database connection
    """
    with conn.cursor() as cur:
        cur.execute(CREATE_EXTENSION_QUERY)
        print("✅ pgvector extension enabled (if not already).")


def create_tables(conn):
    """
    Create necessary tables with pgvector support and metadata validation.
    
    Args:
        conn (psycopg2.connection): Database connection
        
    Note:
        This creates both the validation function and the chunks table
    """
    with conn.cursor() as cur:
        # First create the validation function
        cur.execute(CREATE_METADATA_CHECK)
        # Then create the table with the constraint
        cur.execute(CREATE_TABLE_QUERY)
        print("✅ Tables created successfully with pgvector support and metadata validation!")


def insert_chunk(conn, text, vector, metadata):
    """
    Insert a new chunk into the database.
    
    Args:
        conn (psycopg2.connection): Database connection
        text (str): Chunk text content
        vector (list): Embedding vector (3072 dimensions)
        metadata (dict or str): Metadata as dictionary or JSON string
        
    Returns:
        int: The ID of the inserted chunk
        
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
    """
    Validate and insert multiple chunks in a single transaction.
    
    Args:
        conn (psycopg2.connection): Database connection
        chunks (list[dict]): List of dictionaries containing text, vector, and metadata
        
    Returns:
        list[int]: List of inserted chunk IDs
        
    Raises:
        Exception: If validation or insertion fails
    """
    chunk_ids = []
    
    try:
        with conn.cursor() as cur:
            for chunk in chunks:
                # Validate each chunk using the Pydantic model
                validated_chunk = validate_chunk(chunk)
                cur.execute(INSERT_CHUNK_QUERY, (
                    validated_chunk.text,
                    validated_chunk.vector,
                    json.dumps(validated_chunk.metadata)
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


def search_similar_chunks(conn, query_text: str, limit: int = 5):
    """
    Search for chunks similar to the query text using vector similarity.
    
    Args:
        conn (psycopg2.connection): Database connection
        query_text (str): The text to find similar chunks for
        limit (int, optional): Maximum number of results to return. Defaults to 5.
        
    Returns:
        list[dict]: List of dictionaries containing text, metadata, and similarity score
    """
    # Generate embedding for the query text
    query_embedding = get_embedding(query_text)
    
    # SQL query using cosine distance (1 - cosine similarity)
    search_query = """
        SELECT 
            text,
            metadata,
            1 - (vector <=> %s::vector) as similarity
        FROM chunks
        ORDER BY similarity DESC
        LIMIT %s;
    """
    
    with conn.cursor() as cur:
        cur.execute(search_query, (query_embedding, limit))
        results = cur.fetchall()
        
        # Format results as dictionaries
        similar_chunks = [
            {
                "text": row[0],
                "metadata": row[1],
                "similarity": row[2]
            }
            for row in results
        ]
        
        return similar_chunks

def inspect_database():
    """
    Inspect the database structure and content.
    
    This function:
    1. Opens a connection to the database
    2. Queries the number of rows in the chunks table
    3. Gets the column names and data types of the chunks table
    4. Examines the metadata fields used in the table
    
    Note:
        This is primarily a diagnostic function for development and debugging
    """
    import json
    
    try:
        # Open connection
        conn = get_connection()
        print("✅ Connected to database successfully")
        
        with conn.cursor() as cur:
            # Get row count
            cur.execute("SELECT COUNT(*) FROM chunks")
            row_count = cur.fetchone()[0]
            print(f"📊 Table contains {row_count} rows")
            
            # Get column names and types
            cur.execute("""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = 'chunks'
                ORDER BY ordinal_position
            """)
            columns = cur.fetchall()
            print("\n📋 Table columns:")
            for col in columns:
                print(f"  • {col[0]} ({col[1]})")
            
            # Get metadata fields if table has data
            if row_count > 0:
                cur.execute("""
                    SELECT metadata 
                    FROM chunks 
                    LIMIT 10
                """)
                metadata_samples = cur.fetchall()
                
                # Collect all unique metadata keys
                all_keys = set()
                for row in metadata_samples:
                    # Handle both string and dict formats
                    md = row[0]
                    if isinstance(md, str):
                        md = json.loads(md)
                    
                    all_keys.update(md.keys())
                
                print("\n🔑 Metadata fields found in samples:")
                for key in sorted(all_keys):
                    print(f"  • {key}")
                
                # Show a complete metadata example
                print("\n📝 Sample metadata record:")
                sample = metadata_samples[0][0]
                if isinstance(sample, str):
                    sample = json.loads(sample)
                
                for key, value in sample.items():
                    print(f"  • {key}: {value}")
            
        conn.close()
        print("\n✅ Database inspection complete")
        
    except Exception as e:
        print(f"❌ Error during database inspection: {e}")

# Execute the inspection function if this module is run directly
if __name__ == "__main__":
    inspect_database()