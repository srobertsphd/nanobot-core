from app.database.std_sql_db import get_connection, validate_and_upsert_chunk



try:
    conn = get_connection()
    conn.autocommit = True  # Automatically commit each statement

    # enable_pgvector_extension(conn)
    # create_tables(conn)

    # Example data to insert
    example_chunk_data = {
        "text": "This is a sample chunk of text.",
        "vector": [0.0] * 1536,  # Example vector with 1536 float elements
        "metadata": {
            "filename": "example_file.txt",
            "page_numbers": [1, 2, 3],
            "title": "Example Title"
        }
    }

    # Validate and upsert the chunk
    chunk_id = validate_and_upsert_chunk(conn, example_chunk_data)
    print(f"Inserted chunk with ID: {chunk_id}")

except Exception as e:
    print(f"❌ Error during database setup: {e}")
finally:
    if conn is not None:
        conn.close()
        print("🔌 Database connection closed.")