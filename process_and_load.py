"""
Document processing and database loading script.

This script processes documents and loads them into the database.

Usage:
  python -m process_and_load file.pdf    ## Process a single file
  python -m process_and_load --all       ## Process all files (requires explicit flag)
"""

import sys
import os

from app.document_conversion.document_pipeline import process_document
from app.utils.file_handling import get_files_from_base_path
from app.database.std_sql_db import (
    get_connection,
    create_tables,
    bulk_validate_and_insert_chunks,
    enable_pgvector_extension,
)

# Default directory for documents
DEFAULT_DOCS_DIR = "/home/sng/nanobot-poc/data/original"

# TODO need to add the chunking strategy to the process_document function
def process_file(conn, file_path):
    """Process a single file and load it into the database."""
    print(f"\n=== Processing {file_path} ===")
    chunks_with_embeddings = process_document(file_path)
    id_list = bulk_validate_and_insert_chunks(conn, chunks_with_embeddings)
    print(f"Inserted {len(id_list)} chunks into database")
    return len(id_list)

def main():
    """Main processing function."""
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Error: Missing argument")
        print("Usage:")
        print("  python -m process_data_and_load_db file.pdf  # Process a single file")
        print("  python -m process_data_and_load_db --all     # Process all files")
        return
    
    # Initialize database
    conn = get_connection()
    enable_pgvector_extension(conn)
    create_tables(conn)
    
    # Process based on argument
    arg = sys.argv[1]
    
    if arg == "--all":
        # Process all files (explicit flag required)
        print(f"Processing all files in {DEFAULT_DOCS_DIR}")
        files = get_files_from_base_path(DEFAULT_DOCS_DIR)
        
        if not files:
            print("No files found!")
            return
            
        print(f"Found {len(files)} files to process")
        
        total_chunks = 0
        for file in files:
            chunks = process_file(conn, file)
            total_chunks += chunks
            
        print(f"\nAll documents processed! Inserted {total_chunks} total chunks into database.")
    
    else:
        # Process single file
        file_path = arg
        if not os.path.isfile(file_path):
            print(f"Error: File not found: {file_path}")
            return
            
        process_file(conn, file_path)
        print("\nFile processing complete!")

if __name__ == "__main__":
    main()



