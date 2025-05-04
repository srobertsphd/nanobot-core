"""
Document processing pipeline.

Provides a simplified API for the complete document processing workflow
by using the DocumentService.
"""

from app.services.document_service import DocumentService
from app.database.common import get_connection
from app.database.insert import bulk_validate_and_insert_chunks

# Create a singleton instance
document_service = DocumentService()

def convert_document(doc_path: str, save_intermediate: bool = True):
    """Convert a document to docling format."""
    return document_service.convert_document(doc_path, save_intermediate)

def process_document_for_preview(doc_path: str, chunking_strategy: str = "default", save_intermediate: bool = True):
    """Process a document and return chunks for preview before embedding."""
    # Convert document
    converted_doc = document_service.convert_document(doc_path, save_intermediate)
    
    # Chunk the converted document
    return document_service.chunk_document(converted_doc, chunking_strategy)

def embed_and_upload_chunks(chunks, conn=None):
    """Add embeddings to chunks and upload them to the database."""
    print(f"Adding embeddings to {len(chunks)} chunks...")
    chunks_with_embeddings = document_service.get_embeddings_for_chunks(chunks)
    
    # Create connection if not provided
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True
    
    try:
        print("Uploading chunks to database...")
        chunk_ids = bulk_validate_and_insert_chunks(conn, chunks_with_embeddings)
        print(f"✅ Successfully uploaded {len(chunk_ids)} chunks to database")
        return chunk_ids
    finally:
        # Close connection if we created it
        if close_conn and conn:
            conn.close()

def process_document(doc_path: str, chunking_strategy: str = "default", save_intermediate: bool = True):
    """Process a document with the specified chunking strategy."""
    # Process document to get chunks
    chunks = process_document_for_preview(doc_path, chunking_strategy, save_intermediate)
    
    # Add embeddings and upload to database
    return embed_and_upload_chunks(chunks) 