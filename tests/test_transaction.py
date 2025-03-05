"""
Tests for the transaction management system.
"""

import pytest
import time
import json
import logging
from app.database.transaction import transaction, execute_with_transaction, TransactionTimeout
from app.services.openai_service import get_embedding
from app.config.settings import reload_settings

# Configure logging for tests
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module", autouse=True)
def setup_module():
    """Setup for all tests in this module."""
    # Reload settings to ensure we have the latest values
    reload_settings()
    yield

def insert_test_chunk(conn, text):
    """Insert a test chunk into the database."""
    vector = get_embedding(text)
    metadata = {
        "filename": "test.txt",
        "page_numbers": [1],
        "title": "Test Document",
        "headings": ["Test"],
        "chunking_strategy": "default"
    }
    
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO chunks (text, vector, metadata)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (
            text,
            vector,
            json.dumps(metadata)
        ))
        chunk_id = cur.fetchone()[0]
    
    return chunk_id

def test_normal_transaction():
    """Test a normal transaction."""
    with transaction(feedback=True) as conn:
        chunk_id = insert_test_chunk(conn, "This is a normal transaction test.")
        assert chunk_id is not None
        
        # Verify the chunk was inserted
        with conn.cursor() as cur:
            cur.execute("SELECT text FROM chunks WHERE id = %s", (chunk_id,))
            result = cur.fetchone()
            assert result is not None
            assert result[0] == "This is a normal transaction test."

def test_timeout_transaction():
    """Test a transaction with timeout."""
    # Set a very short timeout to trigger a timeout error
    with pytest.raises(TransactionTimeout):
        with transaction(timeout=0.001, feedback=True) as conn:
            # Sleep to ensure timeout
            time.sleep(0.1)
            insert_test_chunk(conn, "This should timeout.")

def test_error_transaction():
    """Test a transaction with an error."""
    with pytest.raises(Exception):
        with transaction(feedback=True) as conn:
            # Intentionally cause an error
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM non_existent_table")

def test_helper_function():
    """Test the execute_with_transaction helper."""
    chunk_id = execute_with_transaction(
        insert_test_chunk,
        "This is a helper function test.",
        feedback=True
    )
    assert chunk_id is not None
    
    # Verify the chunk was inserted
    with transaction() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT text FROM chunks WHERE id = %s", (chunk_id,))
            result = cur.fetchone()
            assert result is not None
            assert result[0] == "This is a helper function test."

def test_transaction_rollback():
    """Test that transactions are rolled back on error."""
    # Insert a unique text that we can search for
    unique_text = f"Unique rollback test text {time.time()}"
    
    # Try to insert but cause an error
    try:
        with transaction(feedback=True) as conn:
            # First insert a valid chunk
            insert_test_chunk(conn, unique_text)
            
            # Then cause an error
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM non_existent_table")
    except Exception:
        pass  # We expect an exception
    
    # Verify the chunk was NOT inserted (transaction should have rolled back)
    with transaction() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM chunks WHERE text = %s", (unique_text,))
            count = cur.fetchone()[0]
            assert count == 0, "Transaction was not rolled back properly" 