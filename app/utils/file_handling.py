from docling.datamodel.document import ConversionResult
import pickle
from pathlib import Path

def get_files_from_base_path(base_path: str) -> list[str]:
    """
    Gets all files from the base path directory.
    
    Args:
        base_path: Path to directory to scan
        
    Returns:
        list[str]: List of full file paths
    """
    from pathlib import Path
    
    base_dir = Path(base_path)
    files = [str(f) for f in base_dir.glob('*') if f.is_file()]
    return files


def save_processed_document(doc_path: str, docling_document, md_data: str):
    """
    Saves the docling document and markdown data in a new folder under parsed-doc
    
    Args:
        doc_path: Original document path
        docling_document: The docling document object
        md_data: Markdown string data
    """
    # Extract filename without extension
    base_name = Path(doc_path).stem
    
    # Create the target directory
    output_dir = Path("/home/sng/nanobot-poc/data/parsed-doc") / base_name
    # Create the directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save the docling document object using pickle
    docling_path = output_dir / f"{base_name}_docling.pickle"
    with open(docling_path, "wb") as f:
        pickle.dump(docling_document, f)
    
    # Save the markdown data
    md_path = output_dir / f"{base_name}_markdown.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_data)
    
    print(f"Saved processed documents to {output_dir}")
    
def save_docling_and_md(doc_path: str, result: ConversionResult):
    docling_document = result.document
    md_data = docling_document.export_to_markdown()
    save_processed_document(doc_path, docling_document, md_data)