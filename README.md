# Nanobot-POC

## Architecture Pattern

Your project follows a layered architecture:
1. **Presentation Layer**: Streamlit UI in `nanobot_poc.py` 
2. **Service Layer**: Services in `app/services/` that handle business logic
3. **Data Access Layer**: Database interactions in `app/database/`
4. **Utility Layer**: Helper functions in `app/utils/`

## The document processing pipeline follows this flow:
1. Document conversion (using Docling)
2. Text chunking with various strategies
3. Embedding generation (OpenAI)
4. Database storage (PostgreSQL with pgvector)
5. Vector retrieval for similarity search
6. Integration with LLM for RAG (Retrieval-Augmented Generation)

## Key Features
- Multiple chunking strategies for document processing
- Vector similarity search for information retrieval
- Streamlit-based chat interface
- PostgreSQL with pgvector for vector storage
- OpenAI integration for embeddings and chat responses

## Project Structure

### Core Components:
1. **app/** - Main application code
   - **services/** - Service layer with document processing, chunking, and API integrations
     - `document_service.py` - Complete pipeline for document processing
     - `chunking_service.py` - Document chunking strategies
     - `openai_service.py` - OpenAI API integration
     - `prompt_loader.py` - For loading prompt templates
   - **database/** - Database interactions
     - `setup.py` - Database initialization
     - `common.py` - Shared database utilities
     - `insert.py` - Database insertion operations
     - `retrieval.py` - Vector search and retrieval
     - `transaction.py` - Transaction management
     - `maintenance.py` - Database maintenance tasks
   - **models/** - Data models and validators
   - **utils/** - Utility functions
     - File handling, tokenization, logging, etc.
   - **config/** - Configuration settings
   - **prompts/** - Prompt templates

2. **Main Scripts**:
   - `nanobot_poc.py` - Main Streamlit application with UI
   - `process_and_load.py` - CLI tool for processing documents

### Supporting Directories:
- **data/** - Document storage
- **tests/** - Comprehensive test suite
- **examples/** - Example code (has a logging example)
- **notebooks/** - Jupyter notebooks for development and demonstration
- **sandbox/** - Likely for experimentation
- **logs/** - Log files






