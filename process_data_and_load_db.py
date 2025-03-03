from app.config.settings import settings  # noqa: F401
from app.document_conversion.chunking import (
    # simple_docling_convert, 
    chunk_document, 
    process_chunks, 
    get_embeddings_for_chunk_text
)
from app.document_conversion.extract import simple_docling_convert
from app.utils.file_handling import (
    get_files_from_base_path,
    save_docling_and_md
)
from app.database.std_sql_db import (
    get_connection,
    # create_database,
    create_tables,
    bulk_validate_and_insert_chunks,
    enable_pgvector_extension,
)


def process_document(doc_path: str, chunking_strategy: str = "default"):
    """Process a document with the specified chunking strategy.
    
    Args:
        doc_path: Path to the document file
        chunking_strategy: Chunking strategy to use
        
    Returns:
        List of processed chunks with embeddings
    """
    print(f"Docling is now converting {doc_path}...")
    result = simple_docling_convert(doc_path)
    print("saving docling and md...")
    save_docling_and_md(doc_path, result)
    print(f"the type of the result is {type(result)}")
    print(f"Now chunking document using '{chunking_strategy}' strategy...")
    chunks = chunk_document(result, strategy=chunking_strategy)
    print("Now processing chunks...")
    processed_chunks = process_chunks(chunks, chunking_strategy=chunking_strategy)
    print("Now getting embeddings for chunks...")
    processed_chunks_with_embeddings = get_embeddings_for_chunk_text(processed_chunks)
    print(f"Done! Returning {len(processed_chunks_with_embeddings)} chunks with embeddings")
    return processed_chunks_with_embeddings

#------------------------------------------------------------
#       Process all files in the original directory
#------------------------------------------------------------

base_path = "/home/sng/nanobot-poc/data/original"
files = get_files_from_base_path(base_path)

for file in files:
    chunks_with_embeddings = process_document(file)
    
#------------------------------------------------------------
#                 Process a single file
#------------------------------------------------------------

file = "/home/sng/nanobot-poc/data/original/cns-user-manual.pdf"
chunks_with_embeddings = process_document(file)

#------------------------------------------------------------
#               Initialize database connection
#------------------------------------------------------------

# create_database("nanobot_poc")

conn = get_connection()
enable_pgvector_extension(conn)
create_tables(conn)
id_list = bulk_validate_and_insert_chunks(conn, chunks_with_embeddings)



