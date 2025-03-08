# Vector Search

This guide explains how to use NanoBot's vector search capabilities to find relevant information in your processed documents.

## Understanding Vector Search

NanoBot uses vector similarity search to find information in your documents. Unlike traditional keyword search, vector search understands the semantic meaning of your query, allowing it to find relevant information even when the exact words don't match.

### How It Works

1. Your query is converted to a vector embedding using the same model used for document chunks
2. The database finds chunks with vectors most similar to your query vector
3. Results are ranked by similarity score (higher is better)
4. Optional filters can narrow down results by document or chunking strategy

## Basic Search

The simplest way to search is to provide a query text:

```python
from app.database.transaction import transaction
from app.database.db_retrieval import search_similar_chunks

with transaction() as conn:
    results = search_similar_chunks(
        conn=conn,
        query_text="What is machine learning?",
        limit=5  # Return top 5 results
    )
    
    # Display results
    for result in results:
        print(f"Similarity: {result['similarity']:.4f}")
        print(f"Text: {result['text'][:200]}...")
        print("---")
```

## Filtered Search

You can narrow down search results using filters:

```python
from app.database.transaction import transaction
from app.database.db_retrieval import search_similar_chunks_with_filters

with transaction() as conn:
    results = search_similar_chunks_with_filters(
        conn=conn,
        query_text="What is machine learning?",
        limit=5,
        chunking_strategy="balanced",  # Filter by chunking strategy
        filename="machine_learning.pdf"  # Filter by filename
    )
```

### Available Filters

- **chunking_strategy**: Filter by the chunking strategy used when processing the document
- **filename**: Filter by the source document filename

## Getting Metadata

To help with filtering, you can retrieve available metadata values:

```python
from app.database.transaction import transaction
from app.database.db_retrieval import get_chunking_strategies, get_filenames

with transaction() as conn:
    # Get available chunking strategies
    strategies = get_chunking_strategies(conn)
    print(f"Available strategies: {strategies}")
    
    # Get available filenames
    filenames = get_filenames(conn)
    print(f"Available files: {filenames}")
```

## Understanding Search Results

Each search result contains:

- **text**: The content of the chunk
- **similarity**: A score between 0 and 1 indicating how similar the chunk is to your query (higher is better)
- **metadata**: Additional information about the chunk, including:
  - **filename**: The source document
  - **page_numbers**: The pages where this chunk appears
  - **title**: The document title or section heading
  - **headings**: List of headings associated with this chunk
  - **chunking_strategy**: The strategy used to create this chunk

## Using the Streamlit Interface

The Streamlit interface provides a user-friendly way to search your documents:

1. Start the Streamlit app:
   ```bash
   streamlit run nanobot_poc.py
   ```

2. Enter your query in the search box
3. Use the sidebar to configure search parameters:
   - Number of chunks to retrieve
   - Chunking strategy filter
   - Source document filter
4. Click "Search" to execute the query
5. View the results, which include:
   - Chunk text
   - Similarity score
   - Source document and page numbers
   - Other metadata

## Advanced Usage

### Combining with OpenAI

You can use the retrieved chunks as context for OpenAI to generate more comprehensive answers:

```python
from app.services.openai_service import get_chat_response
from app.database.transaction import transaction
from app.database.db_retrieval import search_similar_chunks_with_filters

with transaction() as conn:
    # Search for relevant chunks
    chunks = search_similar_chunks_with_filters(
        conn=conn,
        query_text="What is machine learning?",
        limit=5
    )
    
    # Use chunks as context for OpenAI
    response = get_chat_response(
        prompt="What is machine learning?",
        context_chunks=chunks
    )
    
    print(response)
```

### Performance Considerations

- **Limit**: Adjust the `limit` parameter based on your needs. Higher values return more results but may include less relevant chunks.
- **Filters**: Use filters to narrow down results when you know which documents or chunking strategies are most relevant.
- **Query Formulation**: Be specific in your queries for better results. Vector search works best with clear, focused questions.

## Best Practices

- **Start broad, then narrow**: Begin with unfiltered searches, then add filters if needed
- **Experiment with chunking strategies**: Different strategies work better for different types of queries
- **Use natural language**: Phrase queries as you would ask a human
- **Provide context**: Longer, more detailed queries often yield better results
- **Review metadata**: Check the source document and page numbers to understand where information comes from
