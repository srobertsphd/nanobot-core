"""
Document Service for document processing.

This service provides a complete pipeline for document processing,
from extraction to chunking to embedding.
"""

from app.services.chunking_service import ChunkingService
from app.services.openai_service import get_embedding
from app.utils.file_handling import save_docling_and_md
from docling.document_converter import DocumentConverter

class DocumentService:
    """Service for document processing."""
    
    def __init__(self):
        """Initialize the document service."""
        self.chunking_service = ChunkingService()
        self.converter = DocumentConverter()
    
    def convert_document(self, doc_path: str, save_intermediate: bool = True):
        """Convert a document to docling format."""
        print(f"Docling is now converting {doc_path}...")
        result = self.converter.convert(doc_path)
        
        if save_intermediate:
            print("Saving docling and md...")
            save_docling_and_md(doc_path, result)
        
        print("Document conversion complete!")
        return result
    
    def url_to_markdown(self, url: str):
        """Convert a URL to markdown."""
        return self.converter.url_to_markdown(url)
    
    def chunk_document(self, converted_doc, chunking_strategy: str = "default"):
        """Chunk a converted document using the specified strategy."""
        print(f"Now chunking document using '{chunking_strategy}' strategy...")
        chunks = self.chunking_service.chunk_document(converted_doc.document, strategy=chunking_strategy)
        
        print("Now processing chunks...")
        processed_chunks = self.chunking_service.process_chunks(chunks, chunking_strategy=chunking_strategy)
        
        print(f"Done! Returning {len(processed_chunks)} chunks ready for preview")
        return processed_chunks
    
    def get_embeddings_for_chunks(self, processed_chunks):
        """Add embeddings to processed chunks."""
        total = len(processed_chunks)
        print(f"Getting embeddings for {total} chunks...")
        
        for i, chunk in enumerate(processed_chunks):
            if i % 10 == 0:  # Print progress every 10 chunks
                print(f"Processing embedding {i+1}/{total} ({(i+1)/total*100:.1f}%)")
            vector = get_embedding(chunk.get('text'))
            chunk['vector'] = vector
        
        print(f"Completed embedding generation for all {total} chunks")
        return processed_chunks
    
    def process_document(self, doc_path: str, chunking_strategy: str = "default", save_intermediate: bool = True):
        """Process a document with the complete pipeline."""
        # Convert document
        converted_doc = self.convert_document(doc_path, save_intermediate)
        
        # Chunk the converted document
        chunks = self.chunk_document(converted_doc, chunking_strategy)
        
        # Add embeddings
        chunks_with_embeddings = self.get_embeddings_for_chunks(chunks)
        
        return chunks_with_embeddings 