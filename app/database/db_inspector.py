"""
Database Inspection Utilities

This module provides functions for inspecting and analyzing the contents
of the database, particularly for examining chunks with different properties.
"""

import json
import pandas as pd
import psycopg2.extras
from typing import List, Dict, Any

from app.database.std_sql_db import get_connection

def get_chunks_by_strategy(conn=None, strategy: str = "default") -> List[Dict[str, Any]]:
    """Retrieve all chunks with a specific chunking strategy.
    
    Args:
        conn: Database connection (optional, will create one if not provided)
        strategy: Chunking strategy to filter by
        
    Returns:
        List of dictionaries containing chunk data
    """
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        query = """
            SELECT 
                id,
                text,
                metadata
            FROM chunks
            WHERE metadata->>'chunking_strategy' = %s
            ORDER BY id;
        """
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (strategy,))
            results = cur.fetchall()
            
            # Format results as dictionaries
            chunks = []
            for row in results:
                # Parse metadata from JSON
                metadata = row['metadata']
                if isinstance(metadata, str):
                    metadata = json.loads(metadata)
                    
                chunks.append({
                    "id": row['id'],
                    "text": row['text'],
                    "metadata": metadata
                })
            
            print(f"✅ Retrieved {len(chunks)} chunks with '{strategy}' strategy")
            return chunks
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()

def get_chunks_by_filename(conn=None, filename: str = None) -> List[Dict[str, Any]]:
    """Retrieve all chunks from a specific file.
    
    Args:
        conn: Database connection (optional, will create one if not provided)
        filename: Filename to filter by (can be partial match)
        
    Returns:
        List of dictionaries containing chunk data
    """
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        # Build query based on whether filename is provided
        if filename:
            query = """
                SELECT 
                    id,
                    text,
                    metadata
                FROM chunks
                WHERE metadata->>'filename' LIKE %s
                ORDER BY id;
            """
            params = (f"%{filename}%",)
        else:
            query = """
                SELECT 
                    id,
                    text,
                    metadata
                FROM chunks
                ORDER BY id;
            """
            params = ()
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(query, params)
            results = cur.fetchall()
            
            # Format results as dictionaries
            chunks = []
            for row in results:
                # Parse metadata from JSON
                metadata = row['metadata']
                if isinstance(metadata, str):
                    metadata = json.loads(metadata)
                    
                chunks.append({
                    "id": row['id'],
                    "text": row['text'],
                    "metadata": metadata
                })
            
            if filename:
                print(f"✅ Retrieved {len(chunks)} chunks matching filename '{filename}'")
            else:
                print(f"✅ Retrieved {len(chunks)} total chunks")
            return chunks
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()
            
def get_chunks_by_range(conn=None, start_row: int = 1, end_row: int = 40) -> List[Dict[str, Any]]:
    """Retrieve chunks from the database within a specific row range.
    
    Args:
        conn: Database connection (optional, will create one if not provided)
        start_row: Starting row number (1-based indexing)
        end_row: Ending row number (inclusive)
        
    Returns:
        List of dictionaries containing chunk data
    """
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        # First, get the total number of rows in the database
        count_query = "SELECT COUNT(*) FROM chunks"
        with conn.cursor() as cur:
            cur.execute(count_query)
            total_rows = cur.fetchone()[0]
        
        # Validate input
        if start_row < 1:
            start_row = 1
        if start_row > total_rows:
            print(f"⚠️ Start row {start_row} exceeds database size ({total_rows} rows)")
            return []
        if end_row > total_rows:
            print(f"⚠️ End row adjusted from {end_row} to {total_rows} (database size)")
            end_row = total_rows
        if end_row < start_row:
            end_row = start_row
        
        # Calculate LIMIT and OFFSET
        limit = end_row - start_row + 1
        offset = start_row - 1
        
        query = """
            SELECT 
                id,
                text,
                metadata
            FROM chunks
            ORDER BY id ASC
            LIMIT %s OFFSET %s;
        """
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (limit, offset))
            results = cur.fetchall()
            
            # Format results as dictionaries
            chunks = []
            for row in results:
                # Parse metadata from JSON
                metadata = row['metadata']
                if isinstance(metadata, str):
                    metadata = json.loads(metadata)
                    
                chunks.append({
                    "id": row['id'],
                    "text": row['text'],
                    "metadata": metadata
                })
            
            if chunks:
                print(f"✅ Retrieved chunks {start_row} to {start_row + len(chunks) - 1} of {total_rows} total")
            else:
                print("❌ No chunks retrieved")
            return chunks
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()

def chunks_to_dataframe(chunks: List[Dict[str, Any]]) -> pd.DataFrame:
    """Convert a list of chunks to a pandas DataFrame for analysis.
    
    Args:
        chunks: List of chunk dictionaries
        
    Returns:
        pandas DataFrame with chunk data
    """
    # Extract metadata fields
    rows = []
    for chunk in chunks:
        # Start with basic fields
        row = {
            "id": chunk["id"],
            "text": chunk["text"],
            "text_length": len(chunk["text"]),
        }
        
        # Add all metadata fields with 'meta_' prefix
        for key, value in chunk["metadata"].items():
            row[f"meta_{key}"] = value
            
        rows.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(rows)
    return df

def analyze_chunks(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze a list of chunks and return statistics.
    
    Args:
        chunks: List of chunk dictionaries
        
    Returns:
        Dictionary of statistics
    """
    if not chunks:
        return {"error": "No chunks provided"}
    
    # Basic statistics
    text_lengths = [len(chunk["text"]) for chunk in chunks]
    
    # Collect all metadata fields
    all_metadata_fields = set()
    for chunk in chunks:
        all_metadata_fields.update(chunk["metadata"].keys())
    
    # Count strategies if present
    strategies = {}
    for chunk in chunks:
        strategy = chunk["metadata"].get("chunking_strategy", "unknown")
        strategies[strategy] = strategies.get(strategy, 0) + 1
    
    # Count filenames
    filenames = {}
    for chunk in chunks:
        filename = chunk["metadata"].get("filename", "unknown")
        filenames[filename] = filenames.get(filename, 0) + 1
    
    return {
        "count": len(chunks),
        "text_length": {
            "min": min(text_lengths),
            "max": max(text_lengths),
            "avg": sum(text_lengths) / len(text_lengths),
            "total": sum(text_lengths)
        },
        "metadata_fields": sorted(list(all_metadata_fields)),
        "strategies": strategies,
        "filenames": filenames
    }

def print_chunk_sample(chunks: List[Dict[str, Any]], count: int = 3) -> None:
    """Print a sample of chunks for inspection.
    
    Args:
        chunks: List of chunk dictionaries
        count: Number of chunks to print
    """
    if not chunks:
        print("No chunks to display")
        return
    
    sample = chunks[:count]
    
    for i, chunk in enumerate(sample):
        print(f"\n--- Chunk {i+1}/{count} (ID: {chunk['id']}) ---")
        
        # Print text (truncated if very long)
        text = chunk["text"]
        if len(text) > 200:
            print(f"Text: {text[:197]}...")
        else:
            print(f"Text: {text}")
        
        # Print metadata
        print("Metadata:")
        for key, value in chunk["metadata"].items():
            print(f"  • {key}: {value}")

def inspect_database(conn=None) -> None:
    """Inspect the database structure and content.
    
    Args:
        conn: Database connection (optional, will create one if not provided)
    
    Queries and displays:
    - Number of rows in the chunks table
    - Column names and data types
    - Metadata fields used in the table
    - Sample metadata record
    """
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        print("✅ Connected to database successfully")
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
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
                print(f"  • {col['column_name']} ({col['data_type']})")
            
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
                    md = row['metadata']
                    if isinstance(md, str):
                        md = json.loads(md)
                    
                    all_keys.update(md.keys())
                
                print("\n🔑 Metadata fields found in samples:")
                for key in sorted(all_keys):
                    print(f"  • {key}")
                
                # Show a complete metadata example
                print("\n📝 Sample metadata record:")
                sample = metadata_samples[0]['metadata']
                if isinstance(sample, str):
                    sample = json.loads(sample)
                
                for key, value in sample.items():
                    print(f"  • {key}: {value}")
            
        print("\n✅ Database inspection complete")
        
    except Exception as e:
        print(f"❌ Error during database inspection: {e}")
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()

def compare_chunking_strategies(conn=None, strategies=None, query=None):
    """Compare different chunking strategies.
    
    Args:
        conn: Database connection (optional, will create one if not provided)
        strategies: List of strategies to compare (default: all available)
        query: Query text to use for comparison (optional)
        
    Returns:
        DataFrame with comparison results
    """
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        # Default strategies if none provided
        if strategies is None:
            strategies = ["default", "balanced", "fine_grained", "paragraph"]
        
        # Get chunks for each strategy
        strategy_chunks = {}
        for strategy in strategies:
            chunks = get_chunks_by_strategy(conn, strategy)
            if chunks:
                strategy_chunks[strategy] = chunks
        
        # Create comparison DataFrame
        comparison = []
        for strategy, chunks in strategy_chunks.items():
            stats = analyze_chunks(chunks)
            comparison.append({
                "strategy": strategy,
                "chunk_count": stats["count"],
                "avg_text_length": stats["text_length"]["avg"],
                "min_text_length": stats["text_length"]["min"],
                "max_text_length": stats["text_length"]["max"],
            })
        
        df = pd.DataFrame(comparison)
        
        # If query provided, compare similarity
        if query:
            from app.database.std_sql_db import search_similar_chunks
            
            print(f"Comparing strategy performance for query: '{query}'")
            for strategy in strategies:
                if strategy in strategy_chunks:
                    # Search with limit=1 to get top result for each strategy
                    results = search_similar_chunks(conn, query, limit=1)
                    if results:
                        print(f"\nTop result for '{strategy}' strategy:")
                        print(f"Similarity: {results[0]['similarity']:.4f}")
                        print(f"Text: {results[0]['text'][:200]}...")
        
        return df
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()

def visualize_chunk_distribution(conn=None):
    """Visualize the distribution of chunks by strategy.
    
    Args:
        conn: Database connection (optional, will create one if not provided)
        
    Returns:
        DataFrame with chunk counts by strategy
    """
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # Get counts by strategy
            cur.execute("""
                SELECT 
                    metadata->>'chunking_strategy' as strategy,
                    COUNT(*) as chunk_count
                FROM chunks
                GROUP BY metadata->>'chunking_strategy'
                ORDER BY chunk_count DESC
            """)
            results = cur.fetchall()
            
            # Create DataFrame
            df = pd.DataFrame(results)
            
            # Try to plot if matplotlib is available
            try:
                import matplotlib.pyplot as plt
                
                plt.figure(figsize=(10, 6))
                plt.bar(df['strategy'], df['chunk_count'])
                plt.title('Chunk Distribution by Strategy')
                plt.xlabel('Chunking Strategy')
                plt.ylabel('Number of Chunks')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            except ImportError:
                print("Matplotlib not available for plotting")
            
            return df
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()

# run python -m app.database.db_inspector from the root directory to execute this file
if __name__ == "__main__":
    # When run directly, perform a database inspection
    inspect_database()
    
    # Ask if user wants to see chunks with a specific strategy
    print("\nWould you like to inspect chunks with a specific strategy?")
    response = input("Enter strategy name (or press Enter to skip): ")
    
    if response.strip():
        strategy = response.strip()
        chunks = get_chunks_by_strategy(strategy=strategy)
        
        if chunks:
            # Show analysis
            stats = analyze_chunks(chunks)
            print(f"\n=== Analysis of {stats['count']} chunks with '{strategy}' strategy ===")
            print(f"Text length: min={stats['text_length']['min']}, max={stats['text_length']['max']}, avg={stats['text_length']['avg']:.1f}")
            print(f"Metadata fields: {', '.join(stats['metadata_fields'])}")
            
            # Show sample
            print("\nSample chunks:")
            print_chunk_sample(chunks, count=3) 