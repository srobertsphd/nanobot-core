# from docling.datamodel.document import ConversionResult
from app.document_conversion.chunking import (
    simple_docling_convert, 
    chunk_document, 
    process_chunks, 
    get_embeddings_for_chunk_text
)
from app.document_conversion.utils.file_handling import (
    save_processed_document,
    get_files_from_base_path,
    save_docling_and_md
)
from app.models.validators import validate_chunk
from pprint import pprint

# def save_docling_and_md(doc_path: str, result: ConversionResult):
#     docling_document = result.document
#     md_data = docling_document.export_to_markdown()
#     save_processed_document(doc_path, docling_document, md_data)


def process_document(doc_path: str):
    print(f"Docling is now converting {doc_path}...")
    result = simple_docling_convert(doc_path)
    print("saving docling and md...")
    save_docling_and_md(doc_path, result)
    print(f"the type of the result is {type(result)}")
    print("Now chunking document...")
    chunks = chunk_document(result)
    print("Now processing chunks...")
    processed_chunks = process_chunks(chunks)
    print("Now getting embeddings for chunks...")
    processed_chunks_with_embeddings = get_embeddings_for_chunk_text(processed_chunks)
    print(f"Done! Returning {len(processed_chunks_with_embeddings)} chunks with embeddings")
    return processed_chunks_with_embeddings

base_path = "/home/sng/nanobot-poc/data/original"
files = get_files_from_base_path(base_path)

for file in files:
    chunks_with_embeddings = process_document(file)


chunk = chunks_with_embeddings[5]
pprint(chunk)
type(chunk)

validate_chunk(chunk)
