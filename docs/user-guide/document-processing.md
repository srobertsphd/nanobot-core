# Document Processing

This guide explains how to process documents with NanoBot.

## Supported Document Types

NanoBot supports the following document types:

- PDF (.pdf)
- Microsoft Word (.docx)
- Text files (.txt)

## Processing a Document

You can process documents either through the Streamlit interface or programmatically.

### Using the Streamlit Interface

1. Start the Streamlit app:
   ```bash
   streamlit run nanobot_poc.py
   ```

2. Navigate to the "Upload" section
3. Upload your document
4. Select chunking strategy
5. Click "Process Document"

### Programmatic Processing

```python
from app.database.transaction import transaction
from app.services.document_service import process_document

# Process a document
with transaction() as conn:
    document_id = process_document(
        file_path="path/to/document.pdf",
        chunking_strategy="paragraph",
        conn=conn
    )
    print(f"Processed document with ID: {document_id}")
```

## Chunking Strategies

NanoBot supports several chunking strategies:

- **Paragraph**: Splits text by paragraphs
- **Fixed Size**: Creates chunks of a fixed number of tokens
- **Sentence**: Splits text by sentences
- **Hybrid**: Combines paragraph and sentence splitting

Choose the strategy that works best for your documents and use case.
