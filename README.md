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
