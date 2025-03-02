from docling.chunking import HybridChunker
from docling_core.transforms.chunker.hierarchical_chunker import DocChunk
from openai import OpenAI
from app.utils.tokenizer import OpenAITokenizerWrapper
from app.utils.openai_embedding import get_embedding
from app.config.settings import settings

client = OpenAI(api_key=settings.openai.api_key)

tokenizer = OpenAITokenizerWrapper()
MAX_TOKENS = settings.openai.max_tokens # max tokens for text-embeddding-3-large max context window



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


def get_embeddings_for_chunk_text(processed_chunks):
    for chunk in processed_chunks:
        vector = get_embedding(chunk.get('text'))
        chunk['vector'] = vector
    return processed_chunks


