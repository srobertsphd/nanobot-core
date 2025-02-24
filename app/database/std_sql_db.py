# import os
import psycopg2
from dotenv import load_dotenv
import json
from app.utils.openai_embedding import get_embedding
from app.models.validators import validate_chunk
from app.config.settings import settings

load_dotenv()

# DATABASE_CONFIG = {
#     "dbname": os.getenv("LOCAL_DB_NAME"),
#     "user": os.getenv("LOCAL_DB_USER"),
#     "password": os.getenv("LOCAL_DB_PASSWORD"),
#     "host": os.getenv("LOCAL_DB_HOST"),
#     "port": os.getenv("LOCAL_DB_PORT")
# }

CREATE_EXTENSION_QUERY = """
CREATE EXTENSION IF NOT EXISTS vector;
"""

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

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS chunks (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    vector VECTOR(3072),
    metadata JSONB NOT NULL,
    CONSTRAINT valid_metadata CHECK (validate_chunk_metadata(metadata))
);
"""

INSERT_CHUNK_QUERY = """
    INSERT INTO chunks (text, vector, metadata)
    VALUES (%s, %s, %s)
    RETURNING id;
"""

# def get_connection():
#     """Establish database connection."""
#     try:
#         return psycopg2.connect(**DATABASE_CONFIG)
#     except psycopg2.Error as e:
#         print(f"Error connecting to database: {e}")
#         raise
def get_connection():
    """Establish database connection."""
    try:
        return psycopg2.connect(**settings.local_db.get_connection_dict())
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def create_database(db_name):
    """Create a new database in PostgreSQL."""
    # ADMIN_DATABASE_CONFIG = {
    #     "dbname": os.getenv("LOCAL_DB_ADMIN_NAME"),
    #     "user": os.getenv("LOCAL_DB_ADMIN_USER"),
    #     "password": os.getenv("LOCAL_DB_ADMIN_PASSWORD"),
    #     "host": os.getenv("LOCAL_DB_ADMIN_HOST"),
    #     "port": os.getenv("LOCAL_DB_ADMIN_PORT")
    # }
    # conn = psycopg2.connect(**ADMIN_DATABASE_CONFIG)
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
    """Enable the pgvector extension in PostgreSQL."""
    with conn.cursor() as cur:
        cur.execute(CREATE_EXTENSION_QUERY)
        print("✅ pgvector extension enabled (if not already).")


def create_tables(conn):
    """Create necessary tables in PostgreSQL with pgvector support and metadata validation."""
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
        conn: Database connection
        text: Chunk text
        vector: Embedding vector
        metadata: JSON metadata
    Returns:
        int: The ID of the inserted chunk
    """
    with conn.cursor() as cur:
        cur.execute(INSERT_CHUNK_QUERY, (text, vector, metadata))
        chunk_id = cur.fetchone()[0]
        print(f"✅ Inserted chunk with id: {chunk_id}")
        return chunk_id

def bulk_validate_and_insert_chunks(conn, chunks: list[dict]) -> list[int]:
    """
    Validate and insert multiple chunks using a single database connection.
    
    Args:
        conn: Single database connection used for all operations
        chunks: List of dictionaries containing text, vector, and metadata
        
    Returns:
        list[int]: List of inserted chunk IDs
    """
    chunk_ids = []
    
    try:
        with conn.cursor() as cur:
            for chunk in chunks:
                validated_chunk = validate_chunk(chunk)
                cur.execute(INSERT_CHUNK_QUERY, (
                    validated_chunk.text,
                    validated_chunk.vector,
                    json.dumps(validated_chunk.metadata)
                ))
                chunk_id = cur.fetchone()[0]
                chunk_ids.append(chunk_id)
            
        conn.commit()
        print(f"✅ Successfully processed {len(chunk_ids)} chunks")
        return chunk_ids
        
    except Exception as e:
        print(f"❌ Error in bulk processing: {e}")
        conn.rollback()
        raise


def search_similar_chunks(conn, query_text: str, limit: int = 5):
    """
    Search for chunks similar to the query text using vector similarity.
    """
    query_embedding = get_embedding(query_text)
    
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
        
        similar_chunks = [
            {
                "text": row[0],
                "metadata": row[1],
                "similarity": row[2]
            }
            for row in results
        ]
        
        return similar_chunks