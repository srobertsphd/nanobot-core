"""
Document processing and database loading script.

This script processes documents and loads them into the database.

Usage:
  python -m process_and_load file.pdf                     ## Process a single file with default strategy
  python -m process_and_load file.pdf --strategy balanced ## Process a file with specific strategy
  python -m process_and_load --all                        ## Process all files with default strategy
  python -m process_and_load --all --strategy fine_grained ## Process all files with specific strategy

Available chunking strategies:
  - default: Standard chunking with moderate chunk size
  - balanced: Balanced approach between context preservation and chunk size
  - fine_grained: Smaller chunks for more precise retrieval
  - paragraph: Chunk by paragraphs regardless of size
"""

import sys
import os

from app.services.document_service import DocumentService
from app.utils.file_handling import get_files_from_base_path
from app.database.setup import initialize_database, create_database
from app.config.settings import settings, reload_settings
import psycopg2

# Default directory for documents
DEFAULT_DOCS_DIR = "/home/sng/nanobot-poc/data/original"

# Create document service once
document_service = DocumentService()

def ensure_database_exists():
    """Check if the database exists and create it if it doesn't."""
    # Reload settings to get latest values from .env
    reload_settings()
    
    db_name = settings.local_db.name
    
    # Try to connect to the database using regular credentials
    try:
        conn = psycopg2.connect(**settings.local_db.get_connection_dict())
        conn.close()
        print(f"Database {db_name} already exists.")
    except psycopg2.OperationalError as e:
        # Check if the error is due to the database not existing
        if "does not exist" in str(e):
            print(f"Database {db_name} does not exist. Creating...")
            create_database(db_name)
        else:
            # Other connection error
            print(f"Error connecting to database: {e}")
            raise

def process_file(file_path, chunking_strategy="default"):
    """Process a single file and load it into the database.
    
    Args:
        file_path: Path to the file to process
        chunking_strategy: Strategy to use for chunking (default, balanced, fine_grained, etc.)
    
    Returns:
        Number of chunks inserted into the database
    """
    print(f"\n=== Processing {file_path} with '{chunking_strategy}' strategy ===")
    
    try:
        # Use the document service to handle the entire pipeline
        chunk_ids = document_service.process_and_store_document(
            file_path, 
            chunking_strategy=chunking_strategy
        )
        
        print(f"Inserted {len(chunk_ids)} chunks into database")
        return len(chunk_ids)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return 0

def main():
    """Main processing function."""
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Error: Missing argument")
        print("Usage:")
        print("  python -m process_and_load file.pdf [--strategy STRATEGY]  # Process a single file")
        print("  python -m process_and_load --all [--strategy STRATEGY]     # Process all files")
        return
    
    # Parse arguments
    arg = sys.argv[1]
    chunking_strategy = "default"
    
    # Check for strategy flag
    if "--strategy" in sys.argv:
        strategy_index = sys.argv.index("--strategy")
        if strategy_index + 1 < len(sys.argv):
            chunking_strategy = sys.argv[strategy_index + 1]
            print(f"Using chunking strategy: {chunking_strategy}")
    
    # Ensure database exists
    ensure_database_exists()
    
    # Initialize database
    initialize_database()
    
    # Process based on argument
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
            chunks = process_file(file, chunking_strategy=chunking_strategy)
            total_chunks += chunks
            
        print(f"\nAll documents processed! Inserted {total_chunks} total chunks into database.")
    
    else:
        # Process single file
        file_path = arg
        if not os.path.isfile(file_path):
            print(f"Error: File not found: {file_path}")
            return
            
        process_file(file_path, chunking_strategy=chunking_strategy)
        print("\nFile processing complete!")

if __name__ == "__main__":
    main()



