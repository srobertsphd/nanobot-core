"""
Document Service for document processing.

This service provides a complete pipeline for document processing,
from extraction to chunking to embedding and database operations.
"""

import xml.etree.ElementTree as ET
from app.services.chunking_service import ChunkingService
from app.services.openai_service import get_embedding
from app.utils.file_handling import save_docling_and_md
from docling.document_converter import DocumentConverter
from app.database.common import get_connection
from app.database.insert import bulk_validate_and_insert_chunks


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
    
    def process_document_for_preview(self, doc_path: str, chunking_strategy: str = "default", save_intermediate: bool = True):
        """Process a document and return chunks for preview before embedding."""
        # Convert document
        converted_doc = self.convert_document(doc_path, save_intermediate)
        
        # Chunk the converted document
        return self.chunk_document(converted_doc, chunking_strategy)
    
    def embed_and_upload_chunks(self, chunks, conn=None):
        """Add embeddings to chunks and upload them to the database."""
        print(f"Adding embeddings to {len(chunks)} chunks...")
        chunks_with_embeddings = self.get_embeddings_for_chunks(chunks)
        
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
    
    def process_and_store_document(self, doc_path: str, chunking_strategy: str = "default", save_intermediate: bool = True):
        """Process a document and store chunks in the database."""
        # Process document to get chunks
        chunks = self.process_document_for_preview(doc_path, chunking_strategy, save_intermediate)
        
        # Add embeddings and upload to database
        return self.embed_and_upload_chunks(chunks)
    
    def simple_convert(self, doc_path):
        """Simple conversion by docling. Returns a docling document object"""
        return self.converter.convert(doc_path)
    
    def read_urls_from_sitemap(self, sitemap_path: str) -> list[str]:
        """Read URLs from local sitemap XML file"""
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        
        # Handle namespace in sitemap
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
        
        print(f"Found {len(urls)} URLs in sitemap")
        for url in urls:
            print(f"  - {url}")
            
        return urls
    
    def batch_convert_urls_to_markdown(self, urls: list[str]) -> dict[str, str]:
        """
        Convert a list of URLs to markdown using docling document converter
        
        Args:
            urls: List of URLs to convert
            
        Returns:
            Dictionary mapping URLs to their markdown content
        """
        results = {}
        
        print(f"Converting {len(urls)} URLs to markdown...")
        for url in urls:
            try:
                markdown = self.url_to_markdown(url)
                results[url] = markdown
                print(f"  ✓ Successfully converted {url}")
            except Exception as e:
                print(f"  ✗ Failed to convert {url}: {str(e)}")
                results[url] = None
        
        successful = sum(1 for content in results.values() if content is not None)
        print(f"\nConversion complete: {successful}/{len(urls)} URLs converted successfully")
        
        return results 