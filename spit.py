from app.config.settings import settings, reload_settings
from app.database.db_common import get_connection
from app.database.db_insert import insert_chunk
from app.services.openai_service import get_embedding

import json

# Reload settings to ensure we have the latest values
reload_settings()
print(settings.logfire.token)
# Check which database we're using
print(f"Using Neon database: {settings.use_neon}")


# Get a connection
conn = get_connection()
print("Connected to database")

# Add this to your script to print connection details
print(f"Connected to: {settings.neon_db.db_url}")

# Insert a test chunk
test_text = "This is a test chunk for Neon database."
test_vector = get_embedding(test_text)
test_metadata = {
    "filename": "test.txt",
    "page_numbers": [1],
    "title": "Test Document",
    "headings": ["Test"],
    "chunking_strategy": "default"
}

chunk_id = insert_chunk(
    conn, 
    test_text, 
    test_vector, 
    json.dumps(test_metadata)
)

# Add this line to commit the transaction
conn.commit()

print(f"Inserted chunk with ID: {chunk_id}")

# Verify it was inserted
with conn.cursor() as cur:
    cur.execute("SELECT text FROM chunks WHERE id = %s", (chunk_id,))
    result = cur.fetchone()
    print(f"Retrieved text: {result[0]}")

conn.close()
print("Test completed successfully!")