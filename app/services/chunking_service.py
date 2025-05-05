"""
Chunking Service for document processing.

This service provides different chunking strategies for processing documents,
allowing for fine-grained control over how documents are split into chunks.
"""

from docling.chunking import HybridChunker, HierarchicalChunker
from docling_core.transforms.chunker.hierarchical_chunker import DocChunk
from app.utils.tokenizer import OpenAITokenizerWrapper
from app.config.settings import settings

class ChunkingService:
    """Service for chunking documents using different strategies."""
    
    def __init__(self):
        """Initialize the chunking service with a tokenizer."""
        self.tokenizer = OpenAITokenizerWrapper()
    
    #--------------------------------------------------------------------------
    # Basic Operations - Chunker creation and configuration
    #--------------------------------------------------------------------------
    
    def _get_default_chunker(self):
        """Get the default chunker configuration.
        
        Uses the embedding_max_tokens from settings.
        """
        return HybridChunker(
            tokenizer=self.tokenizer,
            max_tokens=settings.openai.embedding_max_tokens,
            merge_peers=True
        )
    
    def _get_fine_grained_chunker(self):
        """Get a fine-grained chunker for precise semantic search.
        
        Creates smaller, more focused chunks that closely follow document structure.
        """
        return HybridChunker(
            tokenizer=self.tokenizer,
            max_tokens=500,
            merge_peers=False,
            min_chunk_chars=50,
            min_chunk_size_ratio=0.1
        )
    
    def _get_balanced_chunker(self):
        """Get a balanced chunker for general purpose use.
        
        Creates medium-sized chunks that balance structure and context.
        """
        return HybridChunker(
            tokenizer=self.tokenizer,
            max_tokens=1000,
            merge_peers=True,
            min_chunk_chars=100,
            min_chunk_size_ratio=0.25
        )
    
    def _get_context_chunker(self):
        """Get a context-preserving chunker for QA and summarization.
        
        Creates larger chunks that preserve more context.
        """
        return HybridChunker(
            tokenizer=self.tokenizer,
            max_tokens=2000,
            merge_peers=True,
            min_chunk_size_ratio=0.5
        )
    
    def _get_hierarchical_chunker(self):
        """Get a hierarchical chunker that preserves document structure.
        
        Creates chunks based on the document's natural hierarchy.
        """
        return HierarchicalChunker()
    
    #--------------------------------------------------------------------------
    # Mid-level Operations - Strategy selection
    #--------------------------------------------------------------------------
    
    def get_chunker(self, strategy="default"):
        """Get a chunker based on the specified strategy.
        
        Args:
            strategy: One of "default", "fine_grained", "balanced", "context", "hierarchical"
        
        Returns:
            A configured chunker instance
        """
        strategies = {
            "default": self._get_default_chunker,
            "fine_grained": self._get_fine_grained_chunker,
            "balanced": self._get_balanced_chunker,
            "context": self._get_context_chunker,
            "hierarchical": self._get_hierarchical_chunker,
        }
        
        if strategy not in strategies:
            raise ValueError(f"Unknown chunking strategy: {strategy}. Available strategies: {list(strategies.keys())}")
            
        return strategies[strategy]()
    
    #--------------------------------------------------------------------------
    # High-level Operations - Document chunking and metadata extraction
    #--------------------------------------------------------------------------
    
    def chunk_document(self, document, strategy="default") -> list[DocChunk]:
        """Chunk a document using the specified strategy.
        
        Args:
            document: The document to chunk (from docling conversion)
            strategy: The chunking strategy to use
            
        Returns:
            A list of DocChunk objects
        """
        chunker = self.get_chunker(strategy)
        chunk_iter = chunker.chunk(document)
        return list(chunk_iter)
    
    def process_chunks(self, chunks, chunking_strategy="default") -> list[dict]:
        """Extract text, filename, page numbers, and title from the chunks."""
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
                    "title": chunk.meta.headings[0] if chunk.meta.headings else None,
                    "headings": chunk.meta.headings if hasattr(chunk.meta, 'headings') else [],
                    "chunking_strategy": chunking_strategy,
                },
            }
            for chunk in chunks
        ]
        return processed_chunks
    
    def get_available_strategies(self) -> dict:
        """Returns information about available chunking strategies."""
        return {
            "default": "Standard chunking with moderate chunk size",
            "balanced": "Balanced approach between context preservation and chunk size",
            "fine_grained": "Smaller chunks for more precise retrieval",
            "context": "Larger chunks that preserve more context for QA and summarization",
            "hierarchical": "Chunks based on document's natural hierarchy and structure"
        } 