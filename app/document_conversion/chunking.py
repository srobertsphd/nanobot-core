"""
Document chunking utilities.

This module provides functions for chunking documents and processing
the resulting chunks for embedding and storage.
"""
from docling_core.transforms.chunker.hierarchical_chunker import DocChunk
from app.services.openai_service import get_embedding
from app.services.chunking_service import ChunkingService


chunking_service = ChunkingService() #an instance of the ChunkingService class

def chunk_document(result, strategy="default") -> list[DocChunk]:
    """Chunk the document using docling with the specified strategy.
    
    Args:
        result: The result of the docling conversion
        strategy: Chunking strategy to use ("default", "fine_grained", "balanced", "context", "hierarchical")
        
    Returns:
        list[DocChunk]: A list of docling Chunks
    """
    return chunking_service.chunk_document(result.document, strategy)


def process_chunks(chunks, chunking_strategy="default") -> list[dict]:
    """
    Extracts text, filename, page numbers, and title from the chunks.

    Args:
        chunks (list): A list of chunk objects to process.
        chunking_strategy (str): The chunking strategy used.

    Returns:
        list[dict]: A list of dictionaries containing extracted information.
    """
    processed_chunks = [
        {
            "text": chunk.text,
            "metadata": {
                "filename": chunk.meta.origin.filename if hasattr(chunk.meta, 'origin') else "",
                "page_numbers": [
                    page_no
                    for page_no in sorted(
                        set(
                            prov.page_no
                            for item in chunk.meta.doc_items
                            for prov in item.prov
                        )
                    )
                ]
                or None,
                "title": chunk.meta.headings[0] if chunk.meta.headings else None,  # Primary heading
                "headings": chunk.meta.headings if hasattr(chunk.meta, 'headings') else [],  # All relevant headings
                "chunking_strategy": chunking_strategy,
            },
        }
        for chunk in chunks
    ]
    return processed_chunks


def get_embeddings_for_chunk_text(processed_chunks):
    """
    Get embeddings for the text in the processed chunks.

    Args:
        processed_chunks (list): A list of dictionaries containing processed chunks.

    Returns:
        list: A list of dictionaries containing processed chunks with embeddings.
    """
    for chunk in processed_chunks:
        vector = get_embedding(chunk.get('text'))
        chunk['vector'] = vector
    return processed_chunks


def get_available_chunking_strategies() -> dict:
    """
    Returns information about available chunking strategies.
    
    Returns:
        dict: Dictionary mapping strategy names to their descriptions
    """
    return {
        "default": "Standard chunking with moderate chunk size",
        "balanced": "Balanced approach between context preservation and chunk size",
        "fine_grained": "Smaller chunks for more precise retrieval",
        "context": "Larger chunks that preserve more context for QA and summarization",
        "hierarchical": "Chunks based on document's natural hierarchy and structure"
    }