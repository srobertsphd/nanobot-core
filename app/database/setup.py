"""
Database Setup and Initialization

This module provides functions for setting up and initializing the database,
including creating tables, enabling extensions, and setting up indexes.
"""

import psycopg2
from app.config.settings import settings, reload_settings
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
    # Reload settings to ensure we have the latest values
    reload_settings()
    
    # Use admin login information for database creation
    conn = psycopg2.connect(**settings.admin_db.get_connection_dict())
    conn.autocommit = True  
    cur = conn.cursor()

    try:
        cur.execute(f"CREATE DATABASE {db_name}")
        print(f"Database {db_name} created successfully")
        
        # Grant privileges if admin and app users are different
        if settings.admin_db.user != settings.local_db.user:
            cur.execute(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {settings.local_db.user}")
            print(f"Granted privileges on {db_name} to user {settings.local_db.user}")
    except psycopg2.Error as e:
        print(f"Error creating database: {e}")
        raise
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

def initialize_database(use_neon=None):
    """Initialize the database with all required components.
    
    Args:
        use_neon: Override to use Neon database. If None, uses settings.use_neon
    """
    # Reload settings to ensure we have the latest values
    reload_settings()
    
    db_type = "Neon" if (use_neon or (use_neon is None and settings.use_neon)) else "local"
    print(f"Initializing {db_type} database...")
    
    conn = get_connection(use_neon=use_neon)
    try:
        enable_pgvector_extension(conn)
        print(f"✅ pgvector extension enabled in {db_type} database")
        
        create_tables(conn)
        print(f"✅ Tables created in {db_type} database")
        
        create_vector_index(conn)
        print(f"✅ Vector index created in {db_type} database")
        
        conn.commit()
        print(f"✅ {db_type} database initialized successfully")
    except Exception as e:
        conn.rollback()
        print(f"❌ Error initializing {db_type} database: {e}")
        raise
    finally:
        conn.close() 