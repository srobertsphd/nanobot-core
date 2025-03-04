# from docling.document_converter import DocumentConverter
from docling.chunking import HierarchicalChunker, HybridChunker
from app.document_conversion.extract import simple_docling_convert
from app.utils.tokenizer import OpenAITokenizerWrapper

# Path to test PDF
test_pdf_path = "/home/sng/nanobot-poc/data/test/grant_decision_email_single_page.pdf"

# 1. Convert the document using Docling
print("=== CONVERTING DOCUMENT ===")
result = simple_docling_convert(test_pdf_path)
print(f"Document has {len(result.document.pages)} pages")
print(f"Document has {len(result.document.texts)} text elements")

dir(result)
result.schema()
# 2. Examine the document structure
print("\n=== DOCUMENT STRUCTURE ===")
document = result.document

document.dict()

print("Document attributes (data):")
for attr in dir(document):
    if not attr.startswith('_'):  # Skip private attributes
        try:
            value = getattr(document, attr)
            if not callable(value):  # Only non-callable (attributes)
                print(f"- {attr}: {value}")
        except Exception as e:
            print(f"- {attr}: Error accessing ({str(e)})")

print("\nDocument methods (functions):")
for attr in dir(document):
    if not attr.startswith('_'):  # Skip private attributes
        try:
            value = getattr(document, attr)
            if callable(value):  # Only callable (methods)
                print(f"- {attr}()")
        except Exception as e:
            print(f"- {attr}: Error accessing ({str(e)})")



callable(getattr(document, 'schema'))

for attr in dir(document):
    if callable(getattr(document, attr)):
        print(f"- {attr}: {getattr(document, attr)}")


# Extract the full text from all text elements
full_text = ""
for text_item in document.texts:
    full_text += text_item.text + " "
    
print(full_text)

tokenizer = OpenAITokenizerWrapper()
print("\n=== TEXT ELEMENTS STRUCTURE ===")
for i, text_item in enumerate(document.texts):
    print(f"\nText Element #{i+1}:")
    
    # Get the type of the text element
    element_type = type(text_item).__name__
    print(f"Type: {element_type}")
    
    # Print text content with length information
    text_length = len(text_item.text)
    token_count = tokenizer.count_tokens(text_item.text)
    print(f"Text ({text_length} chars, {token_count} tokens): {text_item.text[:100]}..." if text_length > 100 
          else f"Text ({text_length} chars, {token_count} tokens): {text_item.text}")
    
    # Print other attributes based on the element type
    if hasattr(text_item, 'label'):
        print(f"Label: {text_item.label}")
    
    if hasattr(text_item, 'level') and element_type == 'SectionHeaderItem':
        print(f"Heading Level: {text_item.level}")
    
    if hasattr(text_item, 'prov') and text_item.prov:
        page_numbers = [prov.page_no for prov in text_item.prov]
        print(f"Page Numbers: {page_numbers}")
        
        # Get bounding box information if available
        if hasattr(text_item.prov[0], 'bbox'):
            bbox = text_item.prov[0].bbox
            print(f"Bounding Box: left={bbox.l}, top={bbox.t}, right={bbox.r}, bottom={bbox.b}")
    
    # For list items, show list information
    if element_type == 'ListItem':
        if hasattr(text_item, 'list_type'):
            print(f"List Type: {text_item.list_type}")
        if hasattr(text_item, 'list_index'):
            print(f"List Index: {text_item.list_index}")
    
    # Show any other interesting attributes
    for attr in dir(text_item):
        if not attr.startswith('_') and attr not in ['text', 'label', 'level', 'prov', 'list_type', 'list_index']:
            try:
                value = getattr(text_item, attr)
                if not callable(value) and not isinstance(value, (list, dict)) and str(value) != '':
                    print(f"{attr}: {value}")
            except Exception:
                pass

# Extract the full text from all text elements
full_text = ""
for text_item in document.texts:
    full_text += text_item.text + " "
print(f"Total text length: {len(full_text)} characters")
print(f"\nFirst 200 chars of text: {full_text[:200]}...")




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
            print("\n  Example (first chunk):")
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