import streamlit as st
from app.database.std_sql_db import get_connection

def get_unique_metadata_values(conn, field_name):
    """Retrieve unique values for a specific metadata field from the database."""
    try:
        cursor = conn.cursor()
        # Use PostgreSQL JSON operators instead of SQLite's json_extract
        query = f"""
        SELECT DISTINCT metadata->>'{field_name}' as value
        FROM chunks
        WHERE metadata->>'{field_name}' IS NOT NULL
        ORDER BY value
        """
        cursor.execute(query)
        results = cursor.fetchall()
        # Extract values from results and filter out None values
        values = [row[0] for row in results if row[0] is not None]
        return values
    except Exception as e:
        print(f"Error retrieving metadata values for {field_name}: {e}")
        return []

def get_chunking_strategies(conn):
    """Get available chunking strategies from the database."""
    return get_unique_metadata_values(conn, "chunking_strategy")

def get_filenames(conn):
    """Get available filenames from the database."""
    return get_unique_metadata_values(conn, "filename")

def setup_retrieval_sidebar():
    """Setup the sidebar with retrieval configuration options."""
    with st.sidebar:
        st.header("Retrieval Configuration")
        
        # Connect to the database to get metadata options
        conn = get_connection()
        try:
            chunking_strategies = get_chunking_strategies(conn)
            filenames = get_filenames(conn)
        finally:
            conn.close()
        
        # Number of chunks to retrieve
        num_chunks = st.slider(
            "Number of chunks to retrieve", 
            min_value=1, 
            max_value=10, 
            value=5,
            step=1
        )
        
        # Chunking strategy selector
        default_strategy = chunking_strategies[0] if chunking_strategies else "default"
        chunking_strategy = st.selectbox(
            "Chunking Strategy",
            options=chunking_strategies if chunking_strategies else ["default"],
            index=0
        )
        
        # Filename selector
        all_files_option = ["All Files"]
        filename = st.selectbox(
            "Source File",
            options=all_files_option + filenames,
            index=0
        )
        
        # Return the selected configuration
        return {
            "num_chunks": num_chunks,
            "chunking_strategy": None if chunking_strategy == default_strategy else chunking_strategy,
            "filename": None if filename == "All Files" else filename
        } 