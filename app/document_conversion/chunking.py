
from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter
from docling_core.transforms.chunker.hierarchical_chunker import DocChunk
from dotenv import load_dotenv
from openai import OpenAI
from app.document_conversion.utils.tokenizer import OpenAITokenizerWrapper
from app.document_conversion.utils.openai_embedding import get_embedding

# from pprint import pprint
# from pydantic import ValidationError

# import sys
# import os
# # sys.path.append('/path/to/project_root')  
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(parent_dir)
# from models.db_schemas import Chunks, ChunkMetadata

load_dotenv()
client = OpenAI()


doc_path = "/home/sng/nanobot-poc/data/pdf/cns-user-manual.pdf"

tokenizer = OpenAITokenizerWrapper()
MAX_TOKENS = 8191 # max tokens for text-embeddding-3-large max context window


def simple_docling_convert(doc_path) -> DocumentConverter:
    """Simple conversion by docling. Returns a docling document object"""
    converter = DocumentConverter()
    result = converter.convert(doc_path)
    return result

# result = simple_docling_convert(doc_path)

# type(result)

def chunk_document(result) -> list[DocChunk]:
    """Chunk the document using docling. 
    
    Args:
        result (DocumentConverter): The result of the docling conversion

    Returns:
        list[Chunk]: A list of docling Chunks
    """
    chunker = HybridChunker(
        tokenizer=tokenizer,
        max_tokens=MAX_TOKENS,
        merge_peers=True,
    )
    chunk_iter = chunker.chunk(dl_doc=result.document)
    chunks = list(chunk_iter)
    return chunks

# chunks = chunk_document(result)
# type(chunks[0])

def process_chunks(chunks) -> list[dict]:
    """
    Extracts text, filename, page numbers, and title from the chunks.

    Args:
        chunks (list): A list of chunk objects to process.

    Returns:
        list[dict]: A list of dictionaries containing extracted information.
    """
    processed_chunks = [
        {
            "text": chunk.text,
            "metadata": {
                "filename": chunk.meta.origin.filename,
                "page_numbers": [
                    page_no
                    for page_no in sorted(
                        set(
                            prov.page_no
                            for item in chunk.meta.doc_items
                            for prov in item.prov
                        )
                    )
                ]
                or None,
                "title": chunk.meta.headings[0] if chunk.meta.headings else None,
            },
        }
        for chunk in chunks
    ]
    return processed_chunks

# processed_chunks = process_chunks(chunks)
# type(processed_chunks[0])
# pprint(processed_chunks[0])

def get_embeddings_for_chunk_text(processed_chunks):
    for chunk in processed_chunks:
        vector = get_embedding(chunk.get('text'))
        chunk['vector'] = vector
    return processed_chunks

# processed_chunks_with_embeddings = get_embeddings_for_chunk_text(processed_chunks)

# for chunk in processed_chunks:
#     pprint(chunk)
    
# processed_chunks[0]

# processed_chunks[0].get('text')

# for chunk in processed_chunks:
#     vector = get_embedding(chunk.get('text'))
#     chunk['vector'] = vector
    
# test_chunk = processed_chunks_with_embeddings[2]


# try:
#     metadata = ChunkMetadata(**test_chunk['metadata'])
#     print("Metadata is valid:", metadata)
# except ValidationError as e:
#     print("Metadata validation error:", e)

# # Validate chunk
# try:
#     chunk = Chunks(
#         text=test_chunk['text'],
#         vector=test_chunk['vector'],
#         metadata_id=1  # Example metadata_id
#     )
#     print("Chunk is valid:", chunk)
# except ValidationError as e:
#     print("Chunk validation error:", e)

