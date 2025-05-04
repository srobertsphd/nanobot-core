"""
Tests for the Chunking Service.
"""

import os
import pytest
import json
from app.services.chunking_service import ChunkingService
from app.services.document_service import DocumentService
from docling.chunking import HybridChunker, HierarchicalChunker
from app.utils.tokenizer import OpenAITokenizerWrapper

# Sample document path - update with a path that exists in your test environment
SAMPLE_DOC_PATH = "/home/sng/nanobot-poc/data/sample-pdf-files/grant_decision_email_single_page.pdf"

@pytest.fixture
def chunking_service():
    return ChunkingService()

@pytest.fixture
def test_document():
    """Get a test document from a sample PDF."""
    if not os.path.exists(SAMPLE_DOC_PATH):
        pytest.skip(f"Sample document not found at {SAMPLE_DOC_PATH}")
    
    document_service = DocumentService()
    result = document_service.simple_convert(SAMPLE_DOC_PATH)
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
    document_service = DocumentService()
    result = document_service.simple_convert(SAMPLE_DOC_PATH)
    
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

def test_process_chunks_metadata(chunking_service, test_document):
    """Test that process_chunks correctly extracts metadata."""
    # Get chunks using default strategy
    chunks = chunking_service.chunk_document(test_document, "default")
    
    # Process the chunks
    processed_chunks = chunking_service.process_chunks(chunks, "default")
    
    # Verify processed chunks structure
    assert isinstance(processed_chunks, list)
    assert len(processed_chunks) > 0
    
    for chunk in processed_chunks:
        # Check basic structure
        assert "text" in chunk
        assert "metadata" in chunk
        assert isinstance(chunk["metadata"], dict)
        
        # Check metadata fields
        metadata = chunk["metadata"]
        assert "chunking_strategy" in metadata
        assert metadata["chunking_strategy"] == "default"
        
        # These fields should exist but might be None
        assert "filename" in metadata
        assert "page_numbers" in metadata
        assert "title" in metadata
        assert "headings" in metadata

def test_get_available_strategies(chunking_service):
    """Test that get_available_strategies returns the expected dictionary."""
    strategies = chunking_service.get_available_strategies()
    
    # Check that it's a dictionary
    assert isinstance(strategies, dict)
    
    # Check that all expected strategies are present
    expected_strategies = ["default", "balanced", "fine_grained", "context", "hierarchical"]
    for strategy in expected_strategies:
        assert strategy in strategies
        assert isinstance(strategies[strategy], str)
        assert len(strategies[strategy]) > 0

def test_json_serialization(chunking_service, test_document):
    """Test that processed chunks can be serialized to JSON."""
    # Get and process chunks
    chunks = chunking_service.chunk_document(test_document, "default")
    processed_chunks = chunking_service.process_chunks(chunks, "default")
    
    # Try to serialize to JSON
    try:
        json_str = json.dumps(processed_chunks)
        # Deserialize to verify
        deserialized = json.loads(json_str)
        assert len(deserialized) == len(processed_chunks)
    except Exception as e:
        pytest.fail(f"Failed to serialize processed chunks to JSON: {e}")

def test_chunking_consistency(chunking_service, test_document):
    """Test that chunking is consistent when called multiple times with the same parameters."""
    # Get chunks twice with the same strategy
    chunks1 = chunking_service.chunk_document(test_document, "default")
    chunks2 = chunking_service.chunk_document(test_document, "default")
    
    # Check that we get the same number of chunks
    assert len(chunks1) == len(chunks2)
    
    # Check that the text content is the same
    for i in range(len(chunks1)):
        assert chunks1[i].text == chunks2[i].text

@pytest.mark.skip(reason="Need to investigate correct mock structure for empty documents")
def test_chunking_with_empty_document(chunking_service):
    """Test chunking behavior with an empty document."""
    # TODO: Figure out the correct structure for mocking an empty document
    # Current implementation fails because the mock doesn't match what the chunker expects
    class MockDocument:
        def __init__(self):
            self.texts = []
            self.headings = []
            self.lists = []
            self.tables = []
    
    empty_doc = MockDocument()
    
    # Test each strategy with the empty document
    for strategy in ["default", "fine_grained", "balanced", "context", "hierarchical"]:
        # For hierarchical chunker, we need to handle it differently
        if strategy == "hierarchical":
            # Skip hierarchical for empty document as it might require specific structure
            continue
            
        chunks = chunking_service.chunk_document(empty_doc, strategy)
        # Should return an empty list, not fail
        assert isinstance(chunks, list)
        assert len(chunks) == 0

@pytest.mark.skip(reason="Need to investigate correct mock structure for chunks with missing metadata")
def test_process_chunks_with_missing_metadata(chunking_service):
    """Test process_chunks with chunks that have incomplete metadata."""
    # TODO: Figure out the correct structure for mocking chunks with minimal metadata
    # Current implementation fails because the mock doesn't match what process_chunks expects
    class MockChunk:
        def __init__(self):
            self.text = "Test content"
            self.meta = type('MockMeta', (), {
                'headings': [],
                'doc_items': [],
                'origin': None
            })()
    
    # Create a list with our mock chunk
    mock_chunks = [MockChunk()]
    
    # Process the mock chunks
    processed_chunks = chunking_service.process_chunks(mock_chunks, "default")
    
    # Verify it doesn't crash and returns expected structure
    assert len(processed_chunks) == 1
    assert processed_chunks[0]["text"] == "Test content"
    assert "metadata" in processed_chunks[0]
    
    # Check that metadata fields exist with default values
    metadata = processed_chunks[0]["metadata"]
    assert metadata["chunking_strategy"] == "default"
    assert "filename" in metadata
    assert "page_numbers" in metadata
    assert "title" in metadata
    assert "headings" in metadata

@pytest.mark.parametrize("strategy", ["default", "fine_grained", "balanced", "context", "hierarchical"])
def test_strategy_specific_parameters(chunking_service, strategy):
    """Test that each strategy has the expected parameters."""
    chunker = chunking_service.get_chunker(strategy)
    
    if strategy == "hierarchical":
        assert isinstance(chunker, HierarchicalChunker)
    else:
        assert isinstance(chunker, HybridChunker)
        
        # Check strategy-specific parameters that are accessible
        # We can only check max_tokens and merge_peers as they're accessible
        if strategy == "fine_grained":
            assert chunker.max_tokens == 500
            assert chunker.merge_peers is False
        elif strategy == "balanced":
            assert chunker.max_tokens == 1000
            assert chunker.merge_peers is True
        elif strategy == "context":
            assert chunker.max_tokens == 2000
            assert chunker.merge_peers is True
        elif strategy == "default":
            # Default uses settings from config
            from app.config.settings import settings
            assert chunker.max_tokens == settings.openai.embedding_max_tokens
            assert chunker.merge_peers is True 