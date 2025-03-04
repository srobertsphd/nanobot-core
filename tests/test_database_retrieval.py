# from app.config.settings import settings # to activate the settings singleton
from app.database.std_sql_db import get_connection, search_similar_chunks, insert_chunk
from app.services.openai_service import get_embedding

import pytest
import json


@pytest.fixture
def db_connection():
    """Provide a database connection for tests with automatic rollback."""
    # === SETUP PHASE ===
    conn = get_connection()
    
    # Ensure we're in a clean state
    conn.autocommit = True
    
    # Start a new transaction
    conn.autocommit = False
    
    # Create a savepoint at the beginning of the test
    with conn.cursor() as cur:
        cur.execute("SAVEPOINT test_start")
    
    yield conn
    
    # === TEARDOWN PHASE ===
    # Roll back to the savepoint
    with conn.cursor() as cur:
        cur.execute("ROLLBACK TO SAVEPOINT test_start")
    
    # Roll back the entire transaction and close
    conn.rollback()
    conn.close()

@pytest.fixture
def test_data():
    """Provide test data for the tests"""
    return {
        "text": "This is a test document about artificial intelligence and machine learning.",
        "metadata": {
            "filename": "test_document.pdf",
            "page_numbers": [1],
            "title": "Test Document",
            "headings": ["Test Heading"],
            "chunking_strategy": "default"
        }
    }

def test_database_connection(db_connection):
    """Test that we can connect to the database"""
    assert not db_connection.closed, "Database connection should be open"
    
    with db_connection.cursor() as cur:
        cur.execute("SELECT 1")
        result = cur.fetchone()
        assert result[0] == 1, "Simple query should return 1"

def test_table_exists(db_connection):
    """Test that the chunks table exists"""
    with db_connection.cursor() as cur:
        cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'chunks'
            )
        """)
        result = cur.fetchone()
        assert result[0], "Chunks table should exist"

def test_insert_chunk_function(db_connection, test_data):
    """Test the insert_chunk function from std_sql_db.py"""
    # Get embedding for test text
    test_vector = get_embedding(test_data["text"])
    
    # Use the insert_chunk function to insert the test data
    chunk_id = insert_chunk(
        db_connection, 
        test_data["text"], 
        test_vector, 
        json.dumps(test_data["metadata"])
    )
    
    # Verify we got an ID back
    assert chunk_id is not None, "Should get an ID back from insert_chunk"
    
    # Verify the chunk was actually inserted by querying the database directly
    with db_connection.cursor() as cur:
        cur.execute("SELECT text, metadata FROM chunks WHERE id = %s", (chunk_id,))
        result = cur.fetchone()
        
        assert result is not None, "Should be able to retrieve the inserted chunk"
        assert result[0] == test_data["text"], "Retrieved text should match"
        
        # The metadata might be returned as a string or as a dict depending on psycopg2 version
        # So we need to handle both cases
        retrieved_metadata = result[1]
        if isinstance(retrieved_metadata, str):
            retrieved_metadata = json.loads(retrieved_metadata)
        
        assert retrieved_metadata == test_data["metadata"], "Retrieved metadata should match"


def test_vector_similarity_search(db_connection):
    """Test only the vector similarity search functionality"""
    # Insert two test chunks with different content
    test_text1 = "Artificial intelligence is transforming how we interact with computers."
    test_text2 = "Climate change is affecting weather patterns around the world."
    
    print("\nTest documents:")
    print(f"1. AI text: '{test_text1}'")
    print(f"2. Climate text: '{test_text2}'")
    
    # Get embeddings
    vector1 = get_embedding(test_text1)
    vector2 = get_embedding(test_text2)
    
    print(f"\nVector dimensions: AI={len(vector1)}, Climate={len(vector2)}")
    
    # Insert both chunks with complete metadata
    with db_connection.cursor() as cur:
        cur.execute("""
            INSERT INTO chunks (text, vector, metadata)
            VALUES (%s, %s, %s)
        """, (
            test_text1,
            vector1,
            json.dumps({
                "filename": "test1.pdf", 
                "page_numbers": [1], 
                "title": "AI Test",
                "headings": ["AI Heading"],
                "chunking_strategy": "default"
            })
        ))
        
        cur.execute("""
            INSERT INTO chunks (text, vector, metadata)
            VALUES (%s, %s, %s)
        """, (
            test_text2,
            vector2,
            json.dumps({
                "filename": "test2.pdf", 
                "page_numbers": [1], 
                "title": "Climate Test",
                "headings": ["Climate Heading"],
                "chunking_strategy": "default"
            })
        ))
    
    # Search with a query related to AI
    ai_query = "How is AI changing technology?"
    print(f"\nSearch query: '{ai_query}'")
    
    similar_chunks = search_similar_chunks(db_connection, ai_query, limit=2)
    
    # Print the results
    print("\nSearch results (in order of similarity):")
    for i, chunk in enumerate(similar_chunks):
        print(f"Result {i+1}:")
        print(f"  Text: '{chunk['text']}'")
        print(f"  Similarity: {chunk['similarity']:.6f}")
        if 'distance' in chunk:
            print(f"  Distance: {chunk['distance']:.6f}")
    
    # The AI text should be more similar than the climate text
    assert len(similar_chunks) == 2, "Should find two chunks"
    assert similar_chunks[0]["text"] == test_text1, "AI text should be most similar to AI query"
    assert similar_chunks[0]["similarity"] > similar_chunks[1]["similarity"], "AI text should have higher similarity score"
    
    print(f"\nSimilarity difference: {similar_chunks[0]['similarity'] - similar_chunks[1]['similarity']:.6f}")

@pytest.mark.skip(reason="Not fully understood yet - run manually when needed")
def test_chunking_strategy_comparison(db_connection):
    """Compare different chunking strategies."""
    # Test text samples for different chunking strategies
    test_texts = {
        "default": "This is a sample chunk from the default strategy. It contains information about the document.",
        "fine_grained": "This is a smaller chunk from the fine_grained strategy.",
        "balanced": "This is a medium-sized chunk from the balanced strategy. It has a moderate amount of information.",
        "paragraph": "This is a paragraph-based chunk. It respects paragraph boundaries."
    }
    
    # Insert test chunks for each strategy
    for strategy, text in test_texts.items():
        # Get embedding
        vector = get_embedding(text)
        
        # Create metadata
        metadata = {
            "filename": "test_document.pdf",
            "page_numbers": [1],
            "title": "Test Document",
            "headings": ["Test Heading"],  # Add required headings field
            "chunking_strategy": strategy
        }
        
        # Insert chunk
        insert_chunk(
            db_connection, 
            text, 
            vector, 
            json.dumps(metadata)
        )
    
    # Test query
    query = "information about the document"
    
    # Search for similar chunks
    similar_chunks = search_similar_chunks(db_connection, query, limit=3)
    
    # Print results
    print("\nChunking Strategy Comparison Results:")
    for i, chunk in enumerate(similar_chunks):
        strategy = chunk['metadata'].get('chunking_strategy', 'unknown')
        print(f"{i+1}. Strategy: {strategy}, Similarity: {chunk['similarity']:.4f}")
        print(f"   Text: {chunk['text']}")
    
    # Verify we got results
    assert len(similar_chunks) == 3, "Should find all three chunks"
    
    # The default strategy should be most similar for this query
    assert similar_chunks[0]['metadata']['chunking_strategy'] == 'default', "Default strategy should be most similar"