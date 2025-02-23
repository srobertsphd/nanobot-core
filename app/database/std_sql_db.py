import os
import psycopg2
from dotenv import load_dotenv

# import sys
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(project_root)

from app.models.validators import validate_chunk_metadata, validate_chunk


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
CREATE TABLE IF NOT EXISTS chunk_metadata (
    id SERIAL PRIMARY KEY,
    filename TEXT,
    page_numbers INTEGER[],
    title TEXT
);

CREATE TABLE IF NOT EXISTS chunks (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    vector VECTOR(3072), 
    metadata_id INTEGER REFERENCES chunk_metadata(id)
);
"""

UPSERT_CHUNK_METADATA_QUERY = """
    INSERT INTO chunk_metadata (filename, page_numbers, title)
    VALUES (%s, %s, %s)
    ON CONFLICT (filename, title)
    DO UPDATE SET page_numbers = EXCLUDED.page_numbers
    RETURNING id;
"""

UPSERT_CHUNK_QUERY = """
    INSERT INTO chunks (text, vector, metadata_id)
    VALUES (%s, %s, %s)
    ON CONFLICT (text, metadata_id)
    DO UPDATE SET vector = EXCLUDED.vector
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

#create_database("nanobot_poc")

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

        
def upsert_chunk_metadata(conn, filename, page_numbers, title):
    """
    Upsert metadata based on unique filename + title combination.
    Returns the metadata_id.
    """
    with conn.cursor() as cur:
        cur.execute(UPSERT_CHUNK_METADATA_QUERY, (filename, page_numbers, title))
        metadata_id = cur.fetchone()[0]
        print(f"✅ Upserted chunk_metadata with id: {metadata_id}")
        return metadata_id

def upsert_chunk(conn, text, vector, metadata_id):
    """
    Upsert chunk based on text + metadata_id combination.
    If the same text exists for the same metadata, update vector.
    """
    with conn.cursor() as cur:
        cur.execute(UPSERT_CHUNK_QUERY, (text, vector, metadata_id))
        chunk_id = cur.fetchone()[0]
        print(f"✅ Upserted chunk with id: {chunk_id}")
        return chunk_id

    