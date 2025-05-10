from docling.datamodel.document import ConversionResult
import pickle
from pathlib import Path
from app.config.settings import settings
import pandas as pd
from typing import List, Dict, Any

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
    Saves the docling document and markdown data in a new folder under converted_docs
    
    Args:
        doc_path: Original document path
        docling_document: The docling document object
        md_data: Markdown string data
    """
    # Extract filename without extension
    base_name = Path(doc_path).stem
    
    # Create the target directory using settings
    output_dir = settings.file_paths.get_converted_docs_path() / base_name
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

def save_chunk_results(doc_path: str, chunks: list[dict], chunking_strategy: str, 
                      output_dir: str = "data/chunking_results"):
    """
    Saves chunk results including both raw chunks and DataFrame representation.
    
    Args:
        doc_path: Original document path
        chunks: List of chunk dictionaries
        chunking_strategy: The strategy used for chunking
        output_dir: Base directory for saving results
    """
    # Extract filename without extension
    base_name = Path(doc_path).stem
    
    # Create the target directory structure
    strategy_dir = Path(output_dir) / base_name
    strategy_dir.mkdir(parents=True, exist_ok=True)
    
    # Convert chunks to DataFrame
    df = _chunks_to_dataframe(chunks)
    
    # Save DataFrame
    df_path = strategy_dir / f"{chunking_strategy}_chunks.csv"
    df.to_csv(df_path, index=False)
    
    # Save raw chunks
    chunks_path = strategy_dir / f"{chunking_strategy}_chunks.pkl"
    with open(chunks_path, "wb") as f:
        pickle.dump(chunks, f)
    
    print(f"✅ Saved chunk results to {strategy_dir}")

def load_chunk_results(doc_path: str, chunking_strategy: str, 
                      input_dir: str = "data/chunking_results"):
    """
    Load chunk results for a specific document and strategy.
    
    Args:
        doc_path: Original document path
        chunking_strategy: The strategy used for chunking
        input_dir: Base directory for loading results
        
    Returns:
        Tuple of (chunks, DataFrame)
    """
    base_name = Path(doc_path).stem
    strategy_dir = Path(input_dir) / base_name
    
    # Load DataFrame
    df_path = strategy_dir / f"{chunking_strategy}_chunks.csv"
    df = pd.read_csv(df_path)
    
    # Load chunks
    chunks_path = strategy_dir / f"{chunking_strategy}_chunks.pkl"
    with open(chunks_path, 'rb') as f:
        chunks = pickle.load(f)
    
    return chunks, df

def _chunks_to_dataframe(chunks: List[Dict[str, Any]]) -> pd.DataFrame:
    """Convert a list of chunks to a pandas DataFrame."""
    rows = []
    for i, chunk in enumerate(chunks):
        row = {
            "chunk_id": i,
            "text": chunk["text"],
            "text_length": len(chunk["text"])
        }
        
        if "metadata" in chunk:
            metadata = chunk["metadata"]
            for key, value in metadata.items():
                if isinstance(value, list):
                    row[f"meta_{key}"] = ", ".join(str(v) for v in value)
                else:
                    row[f"meta_{key}"] = value
            
        rows.append(row)
    
    return pd.DataFrame(rows)