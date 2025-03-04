"""
Document processing pipeline.

Provides a simplified API for the complete document processing workflow:
extraction → chunking → embedding preparation.

Available chunking strategies:
- default: Standard chunking with moderate chunk size
- balanced: Balanced approach between context preservation and chunk size
- fine_grained: Smaller chunks for more precise retrieval
- paragraph: Chunk by paragraphs regardless of size
"""

from app.document_conversion.extract import simple_docling_convert
from app.document_conversion.chunking import chunk_document, process_chunks, get_embeddings_for_chunk_text
from app.utils.file_handling import save_docling_and_md
from app.database.std_sql_db import get_connection, bulk_validate_and_insert_chunks

def convert_document(doc_path: str, save_intermediate: bool = True):
    """Convert a document to docling format and optionally save intermediate files.
    
    This function handles only the document conversion step, allowing for
    subsequent experimentation with different chunking strategies.
    
    Args:
        doc_path: Path to the document file
        save_intermediate: Whether to save intermediate docling and markdown files
        
    Returns:
        The converted document result from docling
    """
    print(f"Docling is now converting {doc_path}...")
    result = simple_docling_convert(doc_path)
    
    if save_intermediate:
        print("Saving docling and md...")
        save_docling_and_md(doc_path, result)
    
    print("Document conversion complete!")
    return result

def chunk_converted_document(converted_doc, chunking_strategy: str = "default"):
    """Chunk a converted document using the specified strategy.
    
    This function takes a previously converted document and applies
    the specified chunking strategy.
    
    Args:
        converted_doc: The result from convert_document()
        chunking_strategy: Chunking strategy to use
        
    Returns:
        List of processed chunks (without embeddings)
    """
    print(f"Now chunking document using '{chunking_strategy}' strategy...")
    chunks = chunk_document(converted_doc, strategy=chunking_strategy)
    
    print("Now processing chunks...")
    processed_chunks = process_chunks(chunks, chunking_strategy=chunking_strategy)
    
    print(f"Done! Returning {len(processed_chunks)} chunks ready for preview")
    return processed_chunks

def process_document_for_preview(doc_path: str, chunking_strategy: str = "default", save_intermediate: bool = True):
    """Process a document and return chunks for preview before embedding.
    
    This function processes a document up to the chunk processing stage,
    allowing for visualization and analysis before embedding and database upload.
    
    Args:
        doc_path: Path to the document file
        chunking_strategy: Chunking strategy to use
        save_intermediate: Whether to save intermediate docling and markdown files
        
    Returns:
        List of processed chunks (without embeddings)
    """
    # Convert document
    converted_doc = convert_document(doc_path, save_intermediate)
    
    # Chunk the converted document
    return chunk_converted_document(converted_doc, chunking_strategy)


def embed_and_upload_chunks(chunks, conn=None):
    """Add embeddings to chunks and upload them to the database.
    
    Args:
        chunks: List of processed chunks (output from process_document_for_preview)
        conn: Database connection (optional, will create one if not provided)
        
    Returns:
        List of database IDs for the uploaded chunks
    """
    print(f"Adding embeddings to {len(chunks)} chunks...")
    chunks_with_embeddings = get_embeddings_for_chunk_text(chunks)
    
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
    """Process a document with the specified chunking strategy.
    
    This is the complete pipeline that processes a document and uploads it to the database.
    
    Args:
        doc_path: Path to the document file
        chunking_strategy: Chunking strategy to use. Options include:
            - default: Standard chunking with moderate chunk size
            - balanced: Balanced approach between context preservation and chunk size
            - fine_grained: Smaller chunks for more precise retrieval
            - paragraph: Chunk by paragraphs regardless of size
        save_intermediate: Whether to save intermediate docling and markdown files
        
    Returns:
        List of database IDs for the uploaded chunks
    """
    # Process document to get chunks
    chunks = process_document_for_preview(doc_path, chunking_strategy, save_intermediate)
    
    # Add embeddings and upload to database
    return embed_and_upload_chunks(chunks) 