import os
import psycopg2
from dotenv import load_dotenv

# import sys
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(project_root)

from app.models.validators import validate_chunk


load_dotenv()

DATABASE_CONFIG = {
    "dbname": os.getenv("LOCAL_DB_NAME"),
    "user": os.getenv("LOCAL_DB_USER"),
    "password": os.getenv("LOCAL_DB_PASSWORD"),
    "host": os.getenv("LOCAL_DB_HOST"),
    "port": os.getenv("LOCAL_DB_PORT")
}

CREATE_EXTENSION_QUERY = """
CREATE EXTENSION IF NOT EXISTS vector;
"""

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS chunks (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    vector VECTOR(3072),
    metadata JSONB
);
"""

UPSERT_CHUNK_QUERY = """
    INSERT INTO chunks (text, vector, metadata)
    VALUES (%s, %s, %s)
    ON CONFLICT (text, metadata->>'filename', metadata->>'title')
    DO UPDATE SET 
        vector = EXCLUDED.vector,
        metadata = EXCLUDED.metadata
    RETURNING id;
"""

def get_connection():
    """Establish database connection."""
    return psycopg2.connect(**DATABASE_CONFIG)

def create_database(db_name):
    conn = get_connection()
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
    """Enable the pgvector extension in PostgreSQL."""
    with conn.cursor() as cur:
        cur.execute(CREATE_EXTENSION_QUERY)
        print("✅ pgvector extension enabled (if not already).")


def create_tables(conn):
    """Create necessary tables in PostgreSQL with pgvector support."""
    with conn.cursor() as cur:
        cur.execute(CREATE_TABLE_QUERY)
        print("✅ Tables created successfully with pgvector support!")


def upsert_chunk(conn, text, vector, metadata):
    """
    Upsert chunk based on text + metadata combination.
    If the same text exists for the same metadata, update vector.
    """
    conn = get_connection()
    
    with conn.cursor() as cur:
        cur.execute(UPSERT_CHUNK_QUERY, (text, vector, metadata))
        chunk_id = cur.fetchone()[0]
        print(f"✅ Upserted chunk with id: {chunk_id}")
        return chunk_id

def bulk_validate_and_upsert_chunks(conn, chunks: list[dict]) -> list[int]:
    """
    Validate and upsert multiple chunks using a single database connection.
    
    Args:
        conn: Single database connection used for all operations
        chunks: List of dictionaries containing text, vector, and metadata
        
    Returns:
        list[int]: List of inserted chunk IDs
    """
    chunk_ids = []
    
    try:
        # Use the same connection for all operations
        with conn.cursor() as cur:  # Create one cursor for all operations
            for chunk in chunks:
                # Validate chunk
                validated_chunk = validate_chunk(chunk)
                
                # Use the same cursor for each upsert
                cur.execute(UPSERT_CHUNK_QUERY, (
                    validated_chunk.text,
                    validated_chunk.vector,
                    validated_chunk.metadata
                ))
                chunk_id = cur.fetchone()[0]
                chunk_ids.append(chunk_id)
            
        conn.commit()  # Single commit for all operations
        print(f"✅ Successfully processed {len(chunk_ids)} chunks")
        return chunk_ids
        
    except Exception as e:
        print(f"❌ Error in bulk processing: {e}")
        conn.rollback()
        raise
