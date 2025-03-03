"""
Tests for the Chunking Service.
"""

import os
import pytest
from app.services.chunking_service import ChunkingService
from app.document_conversion.extract import simple_docling_convert
from docling.chunking import HybridChunker, HierarchicalChunker
from app.utils.tokenizer import OpenAITokenizerWrapper

# Sample document path - update with a path that exists in your test environment
SAMPLE_DOC_PATH = "/home/sng/nanobot-poc/data/test/grant_decision_email_single_page.pdf"

@pytest.fixture
def chunking_service():
    return ChunkingService()

@pytest.fixture
def test_document():
    """Get a test document from a sample PDF."""
    if not os.path.exists(SAMPLE_DOC_PATH):
        pytest.skip(f"Sample document not found at {SAMPLE_DOC_PATH}")
    
    result = simple_docling_convert(SAMPLE_DOC_PATH)
    return result.document

def test_get_chunker_types(chunking_service):
    """Test that each strategy returns the correct chunker type."""
    assert isinstance(chunking_service.get_chunker("default"), HybridChunker)
    assert isinstance(chunking_service.get_chunker("fine_grained"), HybridChunker)
    assert isinstance(chunking_service.get_chunker("balanced"), HybridChunker)
    assert isinstance(chunking_service.get_chunker("context"), HybridChunker)
    assert isinstance(chunking_service.get_chunker("hierarchical"), HierarchicalChunker)

def test_invalid_strategy(chunking_service):
    """Test that an invalid strategy raises ValueError."""
    with pytest.raises(ValueError):
        chunking_service.get_chunker("nonexistent_strategy")

def test_basic_chunking(chunking_service, test_document):
    """Test that each strategy produces valid chunks."""
    for strategy in ["default", "fine_grained", "balanced", "context", "hierarchical"]:
        chunks = chunking_service.chunk_document(test_document, strategy)
        
        # Basic validation
        assert len(chunks) > 0
        for chunk in chunks:
            assert hasattr(chunk, 'text')
            assert len(chunk.text) > 0
            assert hasattr(chunk, 'meta')

def test_strategy_differences(chunking_service, test_document):
    """Test that different strategies produce different chunking results."""
    # Get chunks for each strategy
    fine_grained_chunks = chunking_service.chunk_document(test_document, "fine_grained")
    balanced_chunks = chunking_service.chunk_document(test_document, "balanced")
    context_chunks = chunking_service.chunk_document(test_document, "context")
    
    # Compare chunk counts - this should generally be true but might not always be
    # depending on the specific document structure
    if len(fine_grained_chunks) > 1 and len(balanced_chunks) > 1:
        assert len(fine_grained_chunks) >= len(balanced_chunks)
    
    if len(balanced_chunks) > 1 and len(context_chunks) > 1:
        assert len(balanced_chunks) >= len(context_chunks)

def test_max_tokens_parameter(chunking_service, test_document):
    """Test that max_tokens parameter affects chunk sizes."""
    tokenizer = OpenAITokenizerWrapper()
    
    # Create custom chunkers with different max_tokens
    small_chunker = HybridChunker(tokenizer=tokenizer, max_tokens=100, merge_peers=True)
    large_chunker = HybridChunker(tokenizer=tokenizer, max_tokens=1000, merge_peers=True)
    
    small_chunks = list(small_chunker.chunk(test_document))
    large_chunks = list(large_chunker.chunk(test_document))
    
    # Smaller max_tokens should produce more chunks or equal (if document is very small)
    assert len(small_chunks) >= len(large_chunks)
    
    # Check token counts
    for chunk in small_chunks:
        token_count = tokenizer.count_tokens(chunk.text)
        # Allow some flexibility due to minimum chunk size requirements
        assert token_count <= 150, f"Chunk exceeds max_tokens by too much: {token_count} > 150"

def test_merge_peers_parameter(chunking_service, test_document):
    """Test that merge_peers parameter affects chunking behavior."""
    tokenizer = OpenAITokenizerWrapper()
    
    # Create custom chunkers with different merge_peers settings
    merge_chunker = HybridChunker(tokenizer=tokenizer, max_tokens=500, merge_peers=True)
    no_merge_chunker = HybridChunker(tokenizer=tokenizer, max_tokens=500, merge_peers=False)
    
    merge_chunks = list(merge_chunker.chunk(test_document))
    no_merge_chunks = list(no_merge_chunker.chunk(test_document))
    
    # Not merging peers should generally produce more chunks
    # This might not always be true for very small documents
    if len(merge_chunks) > 1 and len(no_merge_chunks) > 1:
        assert len(no_merge_chunks) >= len(merge_chunks)

@pytest.mark.skipif(not os.path.exists(SAMPLE_DOC_PATH), reason="Sample document not found")
def test_real_document_chunking(chunking_service):
    """Test chunking with a real document."""
    # Convert the document
    result = simple_docling_convert(SAMPLE_DOC_PATH)
    
    # Test each strategy
    strategies = ["default", "fine_grained", "balanced", "context", "hierarchical"]
    for strategy in strategies:
        chunks = chunking_service.chunk_document(result.document, strategy)
        
        # Basic validation
        assert isinstance(chunks, list)
        
        # Skip further tests if document is empty
        if not result.document.texts:
            continue
            
        # We should have at least one chunk
        assert len(chunks) > 0
        
        # Each chunk should have text
        for chunk in chunks:
            assert hasattr(chunk, 'text')
            assert len(chunk.text) > 0

def print_chunking_results(chunking_service, doc):
    """Helper function to print chunking results for visual inspection."""
    tokenizer = OpenAITokenizerWrapper()
    
    print("\nChunking Results Comparison:")
    print("=" * 80)
    
    for strategy in ["default", "fine_grained", "balanced", "context", "hierarchical"]:
        chunks = chunking_service.chunk_document(doc, strategy)
        
        print(f"\n{strategy.upper()} Strategy - {len(chunks)} chunks")
        print("-" * 40)
        
        for i, chunk in enumerate(chunks):
            token_count = tokenizer.count_tokens(chunk.text)
            print(f"Chunk {i+1}: {len(chunk.text)} chars, {token_count} tokens")
            print(f"Headings: {chunk.meta.headings}")
            preview = chunk.text[:50] + "..." if len(chunk.text) > 50 else chunk.text
            print(f"Preview: {preview}")
            print() 