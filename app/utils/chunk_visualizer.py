"""
Chunk Visualization Utilities

This module provides simple functions for visualizing document chunks
before they are uploaded to the database.
"""

import pandas as pd
from typing import List, Dict, Any

def chunks_to_dataframe(chunks: List[Dict[str, Any]]) -> pd.DataFrame:
    """Convert a list of chunks to a pandas DataFrame for visualization.
    
    Args:
        chunks: List of chunk dictionaries with text and metadata
        
    Returns:
        DataFrame with chunk data
    """
    # Extract metadata fields and flatten them
    rows = []
    for i, chunk in enumerate(chunks):
        # Start with basic chunk info
        row = {
            "chunk_id": i,
            "text": chunk["text"],
            "text_length": len(chunk["text"])
        }
        
        # Add metadata fields
        if "metadata" in chunk:
            metadata = chunk["metadata"]
            for key, value in metadata.items():
                # Handle list values by converting to strings
                if isinstance(value, list):
                    row[f"metadata_{key}"] = ", ".join(str(v) for v in value)
                else:
                    row[f"metadata_{key}"] = value
        
        rows.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(rows)
    
    print(f"✅ Created DataFrame with {len(df)} chunks")
    return df


def display_chunk_samples(df: pd.DataFrame, n_samples: int = 5, text_preview_len: int = 200) -> None:
    """Display sample chunks with truncated text.
    
    Args:
        df: DataFrame of chunks
        n_samples: Number of samples to display
        text_preview_len: Length of text preview
    """
    # Create a copy to avoid modifying the original
    preview_df = df.copy()
    
    # Truncate text for display
    preview_df["text_preview"] = preview_df["text"].str[:text_preview_len] + "..."
    
    # Select columns to display
    display_cols = ["chunk_id", "text_preview", "text_length"]
    
    # Add metadata columns
    metadata_cols = [col for col in preview_df.columns if col.startswith("metadata_")]
    display_cols.extend(metadata_cols)
    
    # Display samples
    print(f"Sample of {n_samples} chunks:")
    return preview_df[display_cols].sample(min(n_samples, len(df))).reset_index(drop=True)
