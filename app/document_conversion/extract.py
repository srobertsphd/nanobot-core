from docling.document_converter import DocumentConverter

def simple_docling_convert(doc_path) -> DocumentConverter:
    """Simple conversion by docling. Returns a docling document object"""
    converter = DocumentConverter()
    result = converter.convert(doc_path)
    return result