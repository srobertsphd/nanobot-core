from app.models.db_schemas import ChunkMetadata, Chunks
from pydantic import ValidationError
import psycopg2
from dotenv import load_dotenv
import os


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

CREATE_TABLE_QUERIES = """
CREATE TABLE IF NOT EXISTS chunk_metadata (
    id SERIAL PRIMARY KEY,
    filename TEXT,
    page_numbers INTEGER[],
    title TEXT
);

CREATE TABLE IF NOT EXISTS chunks (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    vector VECTOR(1536), 
    metadata_id INTEGER REFERENCES chunk_metadata(id)
);
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
        cur.execute(CREATE_TABLE_QUERIES)
        print("✅ Tables created successfully with pgvector support!")

        
def upsert_chunk_metadata(conn, filename, page_numbers, title):
    """
    Upsert metadata based on unique filename + title combination.
    Returns the metadata_id.
    """
    query = """
    INSERT INTO chunk_metadata (filename, page_numbers, title)
    VALUES (%s, %s, %s)
    ON CONFLICT (filename, title)
    DO UPDATE SET page_numbers = EXCLUDED.page_numbers
    RETURNING id;
    """
    with conn.cursor() as cur:
        cur.execute(query, (filename, page_numbers, title))
        metadata_id = cur.fetchone()[0]
        print(f"✅ Upserted chunk_metadata with id: {metadata_id}")
        return metadata_id

def upsert_chunk(conn, text, vector, metadata_id):
    """
    Upsert chunk based on text + metadata_id combination.
    If the same text exists for the same metadata, update vector.
    """
    query = """
    INSERT INTO chunks (text, vector, metadata_id)
    VALUES (%s, %s, %s)
    ON CONFLICT (text, metadata_id)
    DO UPDATE SET vector = EXCLUDED.vector
    RETURNING id;
    """
    with conn.cursor() as cur:
        cur.execute(query, (text, vector, metadata_id))
        chunk_id = cur.fetchone()[0]
        print(f"✅ Upserted chunk with id: {chunk_id}")
        return chunk_id
    
def validate_and_upsert_chunk(conn, chunk_data: dict):
    """
    Validate the entire chunk with Pydantic first, then upsert into DB.
    If validation fails, no DB operations occur.
    """
    try:
        # ✅ Full validation before any DB operation
        validated_chunk = Chunks(**chunk_data)

        # 🔄 Upsert metadata
        metadata_id = upsert_chunk_metadata(
            conn,
            validated_chunk.metadata.filename,
            validated_chunk.metadata.page_numbers,
            validated_chunk.metadata.title
        )

        # 🔄 Upsert chunk
        return upsert_chunk(
            conn,
            validated_chunk.text,
            validated_chunk.vector,
            metadata_id
        )

    except ValidationError as e:
        print(f"❌ Validation failed: {e}")
        raise
    

def main():
    """Main function to connect to the database and set up everything."""
    try:
        conn = get_connection()
        conn.autocommit = True  # Automatically commit each statement

        enable_pgvector_extension(conn)
        create_tables(conn)

    except Exception as e:
        print(f"❌ Error during database setup: {e}")
    finally:
        if conn is not None:
            conn.close()
            print("🔌 Database connection closed.")


if __name__ == "__main__":
    main()