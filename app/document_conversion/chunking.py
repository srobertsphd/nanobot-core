from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter
from dotenv import load_dotenv
from openai import OpenAI
from utils.tokenizer import OpenAITokenizerWrapper
from utils.openai_embedding import get_embedding

load_dotenv()
client = OpenAI()
pdf_path = "/home/sng/nanobot-poc/data/pdf/cns-user-manual.pdf"

tokenizer = OpenAITokenizerWrapper()
MAX_TOKENS = 8191 # max tokens for text-embeddding-3-large max context window

converter = DocumentConverter()
result = converter.convert(pdf_path)

chunker = HybridChunker(
    tokenizer=tokenizer,
    max_tokens=MAX_TOKENS,
    merge_peers=True,
)

chunk_iter = chunker.chunk(dl_doc=result.document)
chunks = list(chunk_iter)


    
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


for chunk in processed_chunks:
    print(chunk)




