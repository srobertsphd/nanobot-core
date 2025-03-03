"""
Document processing pipeline.

Provides a simplified API for the complete document processing workflow:
extraction → chunking → embedding preparation.
"""

from app.document_conversion.extract import simple_docling_convert
from app.document_conversion.chunking import chunk_document, process_chunks, get_embeddings_for_chunk_text
from app.utils.file_handling import save_docling_and_md

def process_document(doc_path: str, chunking_strategy: str = "default", save_intermediate: bool = True):
    """Process a document with the specified chunking strategy.
    
    Args:
        doc_path: Path to the document file
        chunking_strategy: Chunking strategy to use
        save_intermediate: Whether to save intermediate docling and markdown files
        
    Returns:
        List of processed chunks with embeddings
    """
    print(f"Docling is now converting {doc_path}...")
    result = simple_docling_convert(doc_path)
    
    if save_intermediate:
        print("Saving docling and md...")
        save_docling_and_md(doc_path, result)
    
    print(f"Now chunking document using '{chunking_strategy}' strategy...")
    chunks = chunk_document(result, strategy=chunking_strategy)
    
    print("Now processing chunks...")
    processed_chunks = process_chunks(chunks, chunking_strategy=chunking_strategy)
    
    print("Now getting embeddings for chunks...")
    processed_chunks_with_embeddings = get_embeddings_for_chunk_text(processed_chunks)
    
    print(f"Done! Returning {len(processed_chunks_with_embeddings)} chunks with embeddings")
    return processed_chunks_with_embeddings 