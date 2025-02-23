# from database.std_sql_db import get_connection, validate_and_upsert_chunk
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

print(sys.path)
from app.document_conversion.chunking import simple_docling_convert, chunk_document, process_chunks, get_embeddings_for_chunk_text

doc_path = "/home/sng/nanobot-poc/data/pdf/cns-user-manual.pdf"

result = simple_docling_convert(doc_path)

print(result.document.export_to_markdown())

