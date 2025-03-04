"""
Database Maintenance Utilities

This module provides functions for database maintenance operations
such as resetting schemas, cleaning data, and other administrative tasks.
These functions should be used with caution as they can permanently
delete or modify data.
"""

import psycopg2
from app.database.std_sql_db import (
    get_connection,
    CREATE_TABLE_QUERY,
    CREATE_EXTENSION_QUERY,
    CREATE_METADATA_CHECK
)
from app.config.settings import settings

def reset_database_with_new_schema(conn=None, confirm=False):
    """Reset the database with the new schema.
    
    WARNING: This will permanently delete all data in the chunks table.
    
    Args:
        conn: Database connection (optional, will create one if not provided)
        confirm: Set to True to confirm you want to reset the database
        
    Returns:
        True if database was reset, False otherwise
    """
    if not confirm:
        print("⚠️ WARNING: This will permanently delete all data in the chunks table.")
        print("To confirm, call this function with confirm=True")
        return False
    
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        # Step 1: Drop the table
        print("Step 1: Dropping chunks table...")
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS chunks")
            conn.commit()
        
        # Step 2: Enable pgvector extension (in case it's not enabled)
        print("Step 2: Enabling pgvector extension...")
        with conn.cursor() as cur:
            cur.execute(CREATE_EXTENSION_QUERY)
            conn.commit()
        
        # Step 3: Create the metadata validation function
        print("Step 3: Creating metadata validation function...")
        with conn.cursor() as cur:
            cur.execute(CREATE_METADATA_CHECK)
            conn.commit()
        
        # Step 4: Create the table with the new schema
        print("Step 4: Creating chunks table with new schema...")
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_QUERY)
            conn.commit()
        
        # Step 5: Create the vector index based on settings
        print(f"Step 5: Creating {settings.vector_index.index_type} vector index...")
        
        if settings.vector_index.index_type.lower() == "hnsw":
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
            conn.commit()
        
        print("✅ Database has been reset with the new schema")
        print("You can now reprocess your documents with the updated metadata schema")
        return True
    except psycopg2.Error as e:
        print(f"❌ Error resetting database: {e}")
        conn.rollback()
        return False
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()


def clean_chunks_by_strategy(strategy, conn=None, confirm=False):
    """Delete all chunks with a specific chunking strategy.
    
    Args:
        strategy: Chunking strategy to delete
        conn: Database connection (optional, will create one if not provided)
        confirm: Set to True to confirm you want to delete the chunks
        
    Returns:
        Number of chunks deleted
    """
    if not confirm:
        print(f"⚠️ WARNING: This will permanently delete all chunks with '{strategy}' strategy.")
        print("To confirm, call this function with confirm=True")
        return 0
    
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM chunks
                WHERE metadata->>'chunking_strategy' = %s
                RETURNING id
            """, (strategy,))
            
            deleted_ids = cur.fetchall()
            conn.commit()
            
            count = len(deleted_ids)
            print(f"✅ Deleted {count} chunks with '{strategy}' strategy")
            return count
    except psycopg2.Error as e:
        print(f"❌ Error deleting chunks: {e}")
        conn.rollback()
        return 0
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()


def clean_chunks_by_filename(filename, conn=None, confirm=False):
    """Delete all chunks from a specific file.
    
    Args:
        filename: Filename to delete chunks for
        conn: Database connection (optional, will create one if not provided)
        confirm: Set to True to confirm you want to delete the chunks
        
    Returns:
        Number of chunks deleted
    """
    if not confirm:
        print(f"⚠️ WARNING: This will permanently delete all chunks from '{filename}'.")
        print("To confirm, call this function with confirm=True")
        return 0
    
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM chunks
                WHERE metadata->>'filename' = %s
                RETURNING id
            """, (filename,))
            
            deleted_ids = cur.fetchall()
            conn.commit()
            
            count = len(deleted_ids)
            print(f"✅ Deleted {count} chunks from '{filename}'")
            return count
    except psycopg2.Error as e:
        print(f"❌ Error deleting chunks: {e}")
        conn.rollback()
        return 0
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()


def vacuum_database(conn=None):
    """Run VACUUM ANALYZE on the database to reclaim space and update statistics.
    
    Args:
        conn: Database connection (optional, will create one if not provided)
    """
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    # Need to set autocommit for VACUUM
    old_autocommit = conn.autocommit
    conn.autocommit = True
    
    try:
        with conn.cursor() as cur:
            print("Running VACUUM ANALYZE on chunks table...")
            cur.execute("VACUUM ANALYZE chunks")
            print("✅ VACUUM ANALYZE completed")
    except psycopg2.Error as e:
        print(f"❌ Error during VACUUM: {e}")
    finally:
        # Restore previous autocommit setting
        conn.autocommit = old_autocommit
        
        # Close connection if we created it
        if close_conn and conn:
            conn.close()


def update_metadata_field(field_name, old_value, new_value, conn=None, confirm=False):
    """Update a specific metadata field for all matching chunks.
    
    Args:
        field_name: Name of the metadata field to update
        old_value: Current value to match
        new_value: New value to set
        conn: Database connection (optional, will create one if not provided)
        confirm: Set to True to confirm you want to update the chunks
        
    Returns:
        Number of chunks updated
    """
    if not confirm:
        print(f"⚠️ WARNING: This will update the '{field_name}' field from '{old_value}' to '{new_value}'.")
        print("To confirm, call this function with confirm=True")
        return 0
    
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        with conn.cursor() as cur:
            # Use jsonb_set to update the specific field
            cur.execute("""
                UPDATE chunks
                SET metadata = jsonb_set(metadata, %s, %s)
                WHERE metadata->>%s = %s
                RETURNING id
            """, ([field_name], f'"{new_value}"', field_name, old_value))
            
            updated_ids = cur.fetchall()
            conn.commit()
            
            count = len(updated_ids)
            print(f"✅ Updated {count} chunks: '{field_name}' from '{old_value}' to '{new_value}'")
            return count
    except psycopg2.Error as e:
        print(f"❌ Error updating chunks: {e}")
        conn.rollback()
        return 0
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close() 