"""
Document Service for document processing.

This service provides a complete pipeline for document processing,
from extraction to chunking to embedding and database operations.
"""

from app.services.chunking_service import ChunkingService
from app.services.openai_service import get_embedding
from app.utils.file_handling import save_docling_and_md, save_chunk_results
from docling.document_converter import DocumentConverter
from app.database.common import get_connection
from app.database.insert import bulk_validate_and_insert_chunks


class DocumentService:
    """Service for document processing."""
    
    def __init__(self):
        """Initialize the document service."""
        self.chunking_service = ChunkingService()
        self.converter = DocumentConverter()
    
    #--------------------------------------------------------------------------
    # Basic Operations - Core document processing functions
    #--------------------------------------------------------------------------
    
    def convert_document(self, doc_path: str):
        """Convert a document to docling format."""
        print(f"Docling is now converting {doc_path}...")
        result = self.converter.convert(doc_path)
        print("Document conversion complete!")
        return result
    
    
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
    
    #--------------------------------------------------------------------------
    # Mid-level Operations - Combined document processing operations
    #--------------------------------------------------------------------------
    
    def convert_and_chunk_document(self, doc_path: str, chunking_strategy: str = "default", save_intermediate: bool = True):
        """Process a document and return chunks for preview before embedding."""
        # Convert document
        converted_doc = self.convert_document(doc_path)
        
        # Save intermediate docling and md if requested
        if save_intermediate:
            print("Saving docling and md...")
            save_docling_and_md(doc_path, converted_doc)
        
        chunks = self.chunk_document(converted_doc, chunking_strategy)
        
        # Save intermediate chunks if requested
        if save_intermediate:
            save_chunk_results(doc_path, chunks, chunking_strategy)
        
        return chunks

     
    #--------------------------------------------------------------------------
    # High-level Operations - Database interactions and complete pipelines
    #--------------------------------------------------------------------------
    
    def embed_and_upload_chunks(self, chunks, conn=None):
        """Add embeddings to chunks and upload them to the database."""
        # Only call get_embeddings_for_chunks if the chunks don't already have vectors
        if chunks and 'vector' not in chunks[0]:
            print(f"Adding embeddings to {len(chunks)} chunks...")
            chunks = self.get_embeddings_for_chunks(chunks)
        
        # Create connection if not provided
        close_conn = False
        if conn is None:
            conn = get_connection()
            close_conn = True
        
        try:
            print("Uploading chunks to database...")
            chunk_ids = bulk_validate_and_insert_chunks(conn, chunks)
            print(f"✅ Successfully uploaded {len(chunk_ids)} chunks to database")
            return chunk_ids
        finally:
            # Close connection if we created it
            if close_conn and conn:
                conn.close()
    
    def process_and_store_document(self, doc_path: str, chunking_strategy: str = "default", save_intermediate: bool = True):
        """Process a document and store chunks in the database."""
        # Process document to get chunks
        chunks = self.convert_and_chunk_document(doc_path, chunking_strategy, save_intermediate)
        
        # Add embeddings and upload to database
        return self.embed_and_upload_chunks(chunks)
    

    
    