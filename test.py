from app.document_conversion.chunking import simple_docling_convert, chunk_document, process_chunks, get_embeddings_for_chunk_text
from app.models.validators import validate_chunk
from pprint import pprint

doc_path = "/home/sng/nanobot-poc/data/pdf/cns-user-manual.pdf"

result = simple_docling_convert(doc_path)
chunks = chunk_document(result)
chunks[1].model_dump()
processed_chunks = process_chunks(chunks)
processed_chunks_with_embeddings = get_embeddings_for_chunk_text(processed_chunks)

chunk = processed_chunks_with_embeddings[0]
pprint(chunk)
type(chunk)

validate_chunk(chunk)
chunk.get('metadata')
validate_chunk(chunk)