"""
Database Setup and Initialization

This module provides functions for setting up and initializing the database,
including creating tables, enabling extensions, and setting up indexes.
"""

import psycopg2
from app.config.settings import settings
from app.database.common import get_connection
from app.database.schema import (
    CREATE_EXTENSION_QUERY,
    CREATE_METADATA_CHECK,
    CREATE_TABLE_QUERY
)

def create_database(db_name: str) -> None:
    """Create a new PostgreSQL database using admin credentials.
    
    Args:
        db_name: Name of the database to create
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

def enable_pgvector_extension(conn) -> None:
    """Enable the pgvector extension in the PostgreSQL database."""
    with conn.cursor() as cur:
        cur.execute(CREATE_EXTENSION_QUERY)
        print("✅ pgvector extension enabled (if not already).")

def create_tables(conn) -> None:
    """Create necessary tables with pgvector support and metadata validation."""
    with conn.cursor() as cur:
        # First create the validation function
        cur.execute(CREATE_METADATA_CHECK)
        # Then create the table with the constraint
        cur.execute(CREATE_TABLE_QUERY)
        print("✅ Tables created successfully with pgvector support and metadata validation!")

def create_vector_index(conn, index_type=None) -> None:
    """Create a vector index on the chunks table.
    
    Args:
        conn: Database connection
        index_type: Type of index to create ('hnsw' or 'ivfflat')
    """
    index_type = index_type or settings.vector_index.index_type
    
    if index_type.lower() == "hnsw":
        index_query = f"""
            CREATE INDEX IF NOT EXISTS chunks_vector_idx 
            ON chunks 
            USING hnsw (vector vector_cosine_ops)
            WITH (
                m = {settings.vector_index.hnsw_m}, 
                ef_construction = {settings.vector_index.hnsw_ef_construction}
            )
        """
    else:  # Default to ivfflat
        index_query = f"""
            CREATE INDEX IF NOT EXISTS chunks_vector_idx 
            ON chunks 
            USING ivfflat (vector vector_cosine_ops)
            WITH (lists = {settings.vector_index.ivfflat_lists})
        """
        
    with conn.cursor() as cur:
        cur.execute(index_query)
        print(f"✅ Created {index_type} vector index on chunks table")

def initialize_database():
    """Initialize the database with all required components."""
    conn = get_connection()
    try:
        enable_pgvector_extension(conn)
        create_tables(conn)
        create_vector_index(conn)
        conn.commit()
        print("✅ Database initialized successfully")
    except Exception as e:
        conn.rollback()
        print(f"❌ Error initializing database: {e}")
        raise
    finally:
        conn.close()

def initialize_neon_database():
    """Initialize the Neon database with all required components."""
    print("Initializing Neon database...")
    
    # Connect to Neon database
    conn = get_connection(use_neon=True)
    
    try:
        # Enable pgvector extension
        enable_pgvector_extension(conn)
        print("✅ pgvector extension enabled in Neon database")
        
        # Create tables
        create_tables(conn)
        print("✅ Tables created in Neon database")
        
        # Create vector index
        create_vector_index(conn)
        print("✅ Vector index created in Neon database")
        
        # Commit all changes
        conn.commit()
        print("✅ Neon database initialized successfully")
        
        return True
    except Exception as e:
        conn.rollback()
        print(f"❌ Error initializing Neon database: {e}")
        raise
    finally:
        conn.close() 