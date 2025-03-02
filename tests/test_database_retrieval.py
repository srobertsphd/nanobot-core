# from app.config.settings import settings # to activate the settings singleton
from app.database.std_sql_db import get_connection, search_similar_chunks, insert_chunk
from app.services.openai_service import get_embedding

import pytest
import json


@pytest.fixture
def db_connection():
    """Provide a database connection for tests"""
    # === SETUP PHASE ===
    conn = get_connection()
    conn.autocommit = False
    
    yield conn
    
    # === TEARDOWN PHASE ===
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
            "title": "Test Document"
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

def test_get_context_from_db(db_connection, test_data):
    """Test the get_context_from_db function from nanobot_poc.py"""
    # Import the function
    from nanobot_poc import get_context_from_db
    
    # Insert a test chunk
    test_vector = get_embedding(test_data["text"])
    with db_connection.cursor() as cur:
        cur.execute("""
            INSERT INTO chunks (text, vector, metadata)
            VALUES (%s, %s, %s)
        """, (
            test_data["text"],
            test_vector,
            json.dumps(test_data["metadata"])
        ))
    db_connection.commit()  # Commit so get_context_from_db can see it
    
    # Test the function
    context_chunks = get_context_from_db("Tell me about artificial intelligence")
    
    # Verify results
    assert isinstance(context_chunks, list), "Should return a list"
    if len(context_chunks) > 0:
        assert "text" in context_chunks[0], "Chunk should have text"
        assert "metadata" in context_chunks[0], "Chunk should have metadata"
        assert "similarity" in context_chunks[0], "Chunk should have similarity score"

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
    
    # Insert both chunks
    with db_connection.cursor() as cur:
        cur.execute("""
            INSERT INTO chunks (text, vector, metadata)
            VALUES (%s, %s, %s)
        """, (
            test_text1,
            vector1,
            json.dumps({"filename": "test1.pdf", "page_numbers": [1], "title": "AI Test"})
        ))
        
        cur.execute("""
            INSERT INTO chunks (text, vector, metadata)
            VALUES (%s, %s, %s)
        """, (
            test_text2,
            vector2,
            json.dumps({"filename": "test2.pdf", "page_numbers": [1], "title": "Climate Test"})
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
