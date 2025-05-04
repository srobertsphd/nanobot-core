"""
Database Retrieval Operations

This module provides functions for retrieving data from the database,
including vector similarity search and filtered queries.
"""

import json
import psycopg2.extras
from app.services.openai_service import get_embedding


def search_similar_chunks(conn, query_text, limit=5, chunking_strategy=None, filename=None):
    """
    Search for chunks similar to the query text with optional filtering.
    
    Args:
        conn: Database connection
        query_text: The text to search for
        limit: Maximum number of results to return
        chunking_strategy: Filter by chunking strategy (optional)
        filename: Filter by filename (optional)
        
    Returns:
        List of similar chunks with their similarity scores and metadata
    """
    # Generate embedding for the query text
    query_embedding = get_embedding(query_text)
    
    # Print debug information (without vector)
    print(f"Searching with parameters: limit={limit}, chunking_strategy={chunking_strategy}, filename={filename}")
    
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        # First, let's check if we have any chunks in the database
        cursor.execute("SELECT COUNT(*) FROM chunks")
        count = cursor.fetchone()[0]
        print(f"Total chunks in database: {count}")
        
        if count == 0:
            print("No chunks in database, returning empty list")
            return []
        
        # Most basic query - no filters, just vector similarity
        # Cast the embedding array to vector type explicitly
        query = """
        SELECT id, text, metadata, 
               1 - (vector <#> %s::vector) as similarity
        FROM chunks
        ORDER BY similarity DESC
        LIMIT %s
        """
        
        params = [query_embedding, limit]
        
        # Print minimal debug info without the query or parameters
        print("Executing basic similarity search query")
        
        # Execute the query
        cursor.execute(query, params)
        results = cursor.fetchall()
        print(f"Query returned {len(results)} results")
        
        # Process results into a more usable format
        processed_results = []
        for row in results:
            # Convert row to dictionary
            result = dict(row)
            
            # Parse metadata from JSON string if needed
            if isinstance(result['metadata'], str):
                result['metadata'] = json.loads(result['metadata'])
                
            processed_results.append(result)
        
        return processed_results

def search_similar_chunks_with_filters(conn, query_text, limit=5, chunking_strategy=None, filename=None):
    """
    Search for chunks similar to the query text with optional filtering.
    
    Args:
        conn: Database connection
        query_text: The text to search for
        limit: Maximum number of results to return
        chunking_strategy: Filter by chunking strategy (optional)
        filename: Filter by filename (optional)
        
    Returns:
        List of similar chunks with their similarity scores and metadata
    """
    # Generate embedding for the query text
    query_embedding = get_embedding(query_text)
    
    # Print debug information (without vector)
    print(f"Searching with parameters: limit={limit}, chunking_strategy={chunking_strategy}, filename={filename}")
    
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        # First, let's check if we have any chunks in the database
        cursor.execute("SELECT COUNT(*) FROM chunks")
        count = cursor.fetchone()[0]
        print(f"Total chunks in database: {count}")
        
        if count == 0:
            print("No chunks in database, returning empty list")
            return []
        
        # Build query with filters
        base_query = """
        SELECT id, text, metadata, 
               1 - (vector <#> %s::vector) as similarity
        FROM chunks
        WHERE 1=1
        """
        
        params = [query_embedding]  # Start with the embedding parameter
        
        # Add filters if provided
        if chunking_strategy:
            base_query += " AND metadata->>'chunking_strategy' = %s"
            params.append(chunking_strategy)
        
        if filename:
            base_query += " AND metadata->>'filename' = %s"
            params.append(filename)
        
        # Complete the query
        query = base_query + """
        ORDER BY similarity DESC
        LIMIT %s
        """
        
        params.append(limit)
        
        # Print the query for debugging without parameter details
        print("Executing similarity search query with filters")
        
        # Execute the query
        cursor.execute(query, params)
        results = cursor.fetchall()
        print(f"Query returned {len(results)} results")
        
        # Process results into a more usable format
        processed_results = []
        for row in results:
            # Convert row to dictionary
            result = dict(row)
            
            # Parse metadata from JSON string if needed
            if isinstance(result['metadata'], str):
                result['metadata'] = json.loads(result['metadata'])
                
            processed_results.append(result)
        
        return processed_results 

def get_unique_metadata_values(conn, field_name):
    """Retrieve unique values for a specific metadata field from the database."""
    try:
        cursor = conn.cursor()
        # Use PostgreSQL JSON operators
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
    """Get available chunking strategies from the database.
    used in the search_similar_chunks_with_filters function
    """
    return get_unique_metadata_values(conn, "chunking_strategy")

def get_filenames(conn):
    """Get available filenames from the database.
    used in the search_similar_chunks_with_filters function
    """
    return get_unique_metadata_values(conn, "filename") 