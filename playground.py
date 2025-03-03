# from docling.document_converter import DocumentConverter
from docling.chunking import HierarchicalChunker, HybridChunker
from app.document_conversion.extract import simple_docling_convert
from app.document_conversion.chunking import chunk_document, process_chunks
from app.utils.tokenizer import OpenAITokenizerWrapper

# Path to test PDF
test_pdf_path = "/home/sng/nanobot-poc/data/test/grant_decision_email_single_page.pdf"

# 1. Convert the document using Docling
print("=== CONVERTING DOCUMENT ===")
result = simple_docling_convert(test_pdf_path)
print(f"Document has {len(result.document.pages)} pages")
print(f"Document has {len(result.document.texts)} text elements")


# 2. Examine the document structure
print("\n=== DOCUMENT STRUCTURE ===")
document = result.document
# Inspect document attributes safely
print("Document attributes:")
for attr in dir(document):
    if not attr.startswith('_'):  # Skip private attributes
        try:
            value = getattr(document, attr)
            if not callable(value):  # Skip methods
                print(f"- {attr}: {value}")
        except Exception as e:
            print(f"- {attr}: Error accessing ({str(e)})")

print(f"\nFirst 200 chars of text: {document.text[:200]}...")




# 3. Try different chunking methods
# Test different max_tokens values with HybridChunker
print("\n=== CHUNKING EXPERIMENTS ===")
tokenizer = OpenAITokenizerWrapper()
chunking_results = []
for max_tokens in [500, 1000, 2000, 4000]:
    for merge_peers in [True, False]:
        chunker = HybridChunker(
            tokenizer=tokenizer,
            max_tokens=max_tokens,
            merge_peers=merge_peers,
        )
        chunks = list(chunker.chunk(document))
        
        # Calculate statistics
        chunk_sizes = [len(chunk.text) for chunk in chunks]
        token_counts = [tokenizer.count_tokens(chunk.text) for chunk in chunks]
        
        # Add to results
        chunking_results.append({
            'Chunker': 'HybridChunker',
            'max_tokens': max_tokens,
            'merge_peers': merge_peers,
            'num_chunks': len(chunks),
            'avg_chunk_size': sum(chunk_sizes) / len(chunks) if chunks else 0,
            'min_chunk_size': min(chunk_sizes) if chunks else 0,
            'max_chunk_size': max(chunk_sizes) if chunks else 0,
            'avg_token_count': sum(token_counts) / len(token_counts) if token_counts else 0,
            'min_token_count': min(token_counts) if token_counts else 0,
            'max_token_count': max(token_counts) if token_counts else 0,
        })
        
        # Print summary
        print(f"\nHybridChunker with max_tokens={max_tokens}, merge_peers={merge_peers}:")
        print(f"  Number of chunks: {len(chunks)}")
        if chunks:
            print(f"  Average chunk size: {sum(chunk_sizes) / len(chunks):.1f} chars")
            print(f"  Average token count: {sum(token_counts) / len(token_counts):.1f} tokens")
            print(f"  Token count range: {min(token_counts)} - {max(token_counts)}")
            
            # Show first chunk as example
            first_chunk = chunks[0]
            print(f"\n  Example (first chunk):")
            print(f"  - Length: {len(first_chunk.text)} chars, {tokenizer.count_tokens(first_chunk.text)} tokens")
            print(f"  - Text: {first_chunk.text[:100]}...")

print("\n=== HIERARCHICAL CHUNKING (DEFAULT) ===")
hierarchical_chunker = HierarchicalChunker()
hierarchical_chunks = list(hierarchical_chunker.chunk(document))
print(f"Number of hierarchical chunks: {len(hierarchical_chunks)}")
for i, chunk in enumerate(hierarchical_chunks[:3]):  # Show first 3 chunks
    print(f"\nChunk {i+1}:")
    print(f"Text length: {len(chunk.text)} chars")
    print(f"First 100 chars: {chunk.text[:100]}...")
    print(f"Headings: {chunk.meta.headings}")
    print(f"Page numbers: {[prov.page_no for item in chunk.meta.doc_items for prov in item.prov]}")

# 4. Try the app's chunking method (HybridChunker with token limits)
print("\n=== HYBRID CHUNKING (FROM APP) ===")
tokenizer = OpenAITokenizerWrapper()
# Try different max_tokens values
for max_tokens in [500, 1000, 2000]:
    print(f"\n--- With max_tokens={max_tokens} ---")
    hybrid_chunker = HybridChunker(
        tokenizer=tokenizer,
        max_tokens=max_tokens,
        merge_peers=True,
    )
    hybrid_chunks = list(hybrid_chunker.chunk(document))
    print(f"Number of hybrid chunks: {len(hybrid_chunks)}")
    
    # Show first chunk details
    if hybrid_chunks:
        first_chunk = hybrid_chunks[0]
        print(f"First chunk token count: ~{tokenizer.count_tokens(first_chunk.text)}")
        print(f"First chunk text length: {len(first_chunk.text)} chars")
        print(f"First 100 chars: {first_chunk.text[:100]}...")

# 5. Process chunks using the app's method
print("\n=== PROCESSED CHUNKS ===")
app_chunks = chunk_document(result)
processed_chunks = process_chunks(app_chunks)
print(f"Number of processed chunks: {len(processed_chunks)}")
for i, chunk in enumerate(processed_chunks[:2]):  # Show first 2 processed chunks
    print(f"\nProcessed Chunk {i+1}:")
    print(f"Text length: {len(chunk['text'])} chars")
    print(f"First 100 chars: {chunk['text'][:100]}...")
    print(f"Metadata: {chunk['metadata']}")

# 6. Experiment with custom chunking parameters
print("\n=== CUSTOM CHUNKING EXPERIMENT ===")
custom_chunker = HybridChunker(
    tokenizer=tokenizer,
    max_tokens=800,  # Try a different token limit
    merge_peers=False,  # Don't merge peer sections
    min_chunk_chars=100,  # Minimum chunk size in characters
    min_chunk_size_ratio=0.5,  # Minimum chunk size as ratio of max_tokens
)
custom_chunks = list(custom_chunker.chunk(document))
print(f"Number of custom chunks: {len(custom_chunks)}")
for i, chunk in enumerate(custom_chunks[:3]):  # Show first 3 chunks
    print(f"\nCustom Chunk {i+1}:")
    print(f"Text length: {len(chunk.text)} chars")
    print(f"Token count: ~{tokenizer.count_tokens(chunk.text)}")
    print(f"First 100 chars: {chunk.text[:100]}...")