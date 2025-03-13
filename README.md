# nanobot POC

This project will contain the basic elements of Nanobot for document ingestion and vectorization, a basic frontend with a chat interface and retrieval, and a dockerized PostgreSQL database with Timescale vector extension.

## TODO

1.  Integrate transaction handling with the database code
    * Have implemnented the transaction file
    * Have tested using pytest transaction.py
2. Deal with Logging
    * Basic Logging
    * Logfire Logging for LLM and Production
3. Deal with PydanticAI Implementation
    * Will require an LLM factory of some kind?  
4. Set up testing of the RAG system
5. Deal with the Document Ingestion with Docling
6. Set up other services and Factory patterns


```bash
nanobot-poc/
├── app/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db_manager.py
│   │   └── vector_store.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── chunk.py
│   │   ├── document.py
│   │   └── embedding.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chunking_service.py
│   │   ├── document_service.py
│   │   ├── embedding_service.py
│   │   └── vector_store_service.py
│   └── utils/
│       ├── __init__.py
│       ├── file_utils.py
│       ├── logging_config.py
│       └── text_utils.py
├── data/
│   ├── documents/
│   ├── embeddings/
│   └── vectors/
├── docs/
│   ├── api/
│   │   ├── database.md
│   │   └── services.md
│   ├── blog/
│   │   ├── index.md
│   │   └── mkdocs-2025-03-08.md
│   ├── user-guide/
│   │   ├── document-processing.md
│   │   ├── index.md
│   │   └── vector-search.md
│   ├── examples.md
│   ├── getting-started.md
│   └── index.md
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── logs/
├── notebooks/
│   ├── document_processing.ipynb
│   ├── embedding_generation.ipynb
│   └── vector_search.ipynb
├── sandbox/
├── site/
├── tests/
│   ├── __init__.py
│   ├── fixtures/
│   │   ├── sample.docx
│   │   ├── sample.pdf
│   │   └── sample.txt
│   ├── test_chunking_service.py
│   ├── test_document_service.py
│   ├── test_embedding_service.py
│   └── test_vector_store_service.py
├── .cursor/
├── .env
├── .git/
├── .gitignore
├── .pytest_cache/
├── .venv/
├── .vscode/
├── __pycache__/
├── mkdocs.yml
├── nanobot_poc.py
├── process_and_load.py
├── README.md
├── requirements.txt
├── run_logging_example.py
└── spit.py
```