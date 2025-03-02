from yaml import serialize
from app.document_conversion.scraping import (
    read_urls_from_sitemap,
    # batch_convert_urls_to_markdown
)
from docling.document_converter import DocumentConverter
from docling_core.trasforms.chunker import BaseChunker

sitemap_path = "/home/sng/nanobot-poc/data/original/ASRC/nanofab-sitemap.xml"
sitemap_urls = read_urls_from_sitemap(sitemap_path)
print(sitemap_urls)

converter = DocumentConverter()
conv_results_iter = converter.convert_all(sitemap_urls)

docs = []
for result in conv_results_iter:
    if result.document:
        document = result.document
        docs.append(document)

from pprint import pprint
pprint(docs[0].model_dump_json())
print(docs[0].export_to_markdown())

pdf_test = converter.convert("/home/sng/nanobot-poc/data/test/test_pdf_letter_with_images.pdf")
print(pdf_test.document.export_to_markdown())
pprint(pdf_test.document.model_dump_json())