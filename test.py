# from app.database.std_sql_db import get_connection, validate_and_upsert_chunk
from app.document_conversion.chunking import simple_docling_convert, chunk_document, process_chunks, get_embeddings_for_chunk_text
from pprint import pprint
from app.models.validators import validate_chunk, validate_chunk_metadata
# import sys
# import os

# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(project_root)



doc_path = "/home/sng/nanobot-poc/data/pdf/cns-user-manual.pdf"

result = simple_docling_convert(doc_path)
chunks = chunk_document(result)
processed_chunks = process_chunks(chunks)
processed_chunks_with_embeddings = get_embeddings_for_chunk_text(processed_chunks)

chunk = processed_chunks_with_embeddings[0]
pprint(chunk)

validate_chunk_metadata(chunk.get('metadata'))
chunk.get('metadata')
