# Document Processing

This guide explains how NanoBot processes documents, from initial conversion to chunking and embedding.

## Supported Document Types

NanoBot supports various document types through its document conversion pipeline:

- **PDF (.pdf)**: Full support for text extraction, including tables and basic formatting
- **Microsoft Word (.docx)**: Support for text, tables, and document structure
- **Text files (.txt)**: Plain text processing
- **Web Pages (URLs)**: Extract content directly from web pages

## Document Processing Pipeline

The document processing pipeline consists of three main stages:

1. **Document Conversion**: Converting documents to a structured format
2. **Chunking**: Breaking documents into manageable pieces
3. **Embedding**: Generating vector representations for each chunk

### Document Conversion

The first step in processing a document is converting it to a structured format that preserves the document's content and structure. This is handled by the `DocumentService` class using the Docling library.

```python
from app.services.document_service import DocumentService

# Initialize the service
document_service = DocumentService()

# Convert a document
converted_doc = document_service.convert_document("path/to/document.pdf")
```

During conversion, NanoBot:
- Extracts text content
- Preserves document structure (headings, paragraphs)
- Identifies metadata (title, author, etc.)
- Optionally saves intermediate formats for debugging

### Chunking Strategies

After conversion, documents are split into chunks using one of several chunking strategies. Each strategy is optimized for different use cases:

| Strategy | Description | Best For |
|----------|-------------|----------|
| **default** | Standard chunking with moderate chunk size | General purpose use |
| **balanced** | Balanced approach between context preservation and chunk size | Most document types |
| **fine_grained** | Smaller chunks for more precise retrieval | Technical documents, reference materials |
| **context** | Larger chunks that preserve more context | Q&A, summarization tasks |
| **hierarchical** | Chunks based on document's natural hierarchy | Structured documents with clear sections |

The chunking process is handled by the `ChunkingService` class:

```python
from app.services.chunking_service import ChunkingService

# Initialize the service
chunking_service = ChunkingService()

# Get information about available strategies
strategies = chunking_service.get_available_strategies()

# Chunk a document using a specific strategy
chunks = chunking_service.chunk_document(document, strategy="balanced")

# Process chunks to extract metadata
processed_chunks = chunking_service.process_chunks(chunks, chunking_strategy="balanced")
```

### Embedding Generation

The final step is generating vector embeddings for each chunk using OpenAI's embedding models. These embeddings capture the semantic meaning of the text, enabling similarity search.

```python
# Generate embeddings for chunks
chunks_with_embeddings = document_service.get_embeddings_for_chunks(processed_chunks)
```

NanoBot uses OpenAI's text embedding models to generate high-dimensional vector representations of each chunk.

## Complete Processing Example

Here's a complete example of processing a document from start to finish:

```python
from app.database.transaction import transaction
from app.services.document_service import DocumentService

# Initialize the service
document_service = DocumentService()

# Process a document with the complete pipeline
with transaction() as conn:
    chunks_with_embeddings = document_service.process_document(
        doc_path="path/to/document.pdf",
        chunking_strategy="balanced",
        save_intermediate=True
    )
    
    # Now you can insert these chunks into the database
    # (See the database documentation for details)
```

## Using the Streamlit Interface

For a more user-friendly experience, you can use the Streamlit interface to process documents:

1. Start the Streamlit app:
   ```bash
   streamlit run nanobot_poc.py
   ```

2. Navigate to the "Upload" section
3. Upload your document
4. Select a chunking strategy from the dropdown
5. Click "Process Document"

The interface will show progress as the document is processed and provide feedback on the number of chunks created.

## Best Practices

- **Choose the right chunking strategy** for your document type and use case
- **Process similar documents with the same strategy** for consistent results
- **Use meaningful filenames** to help with filtering during retrieval
- **Consider document structure** when choosing a chunking strategy
- **Monitor token usage** when processing large documents
