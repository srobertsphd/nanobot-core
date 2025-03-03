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