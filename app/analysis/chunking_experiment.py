"""
Chunking Experiment Utility

This module provides a class for experimenting with different document chunking strategies,
analyzing the results, and comparing their effectiveness.
"""

import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict, Any, Optional, Tuple

from app.services.document_service import DocumentService
from app.database.common import get_connection
from app.database.insert import bulk_validate_and_insert_chunks


class ChunkingExperiment:
    """Class to manage chunking experiments with different strategies."""
    
    def __init__(self, document_path: Optional[str] = None, 
                 converted_doc: Optional[Dict[str, Any]] = None):
        """Initialize with either a document path or already converted document.
        
        Args:
            document_path: Path to the document file (PDF, DOCX, etc.)
            converted_doc: Already converted document (from convert_document)
        """
        self.document_path = document_path
        self.converted_doc = converted_doc
        self.results = {}
        self.document_service = DocumentService()
        
        # Convert document if path provided and no converted doc
        if document_path and not converted_doc:
            print(f"Converting document: {document_path}")
            self.converted_doc = self.document_service.convert_document(document_path)
            print("✅ Converted document")
    
    def run_strategy(self, strategy: str) -> Dict[str, Any]:
        """Run a single chunking strategy and store results.
        
        Args:
            strategy: Name of chunking strategy to use
            
        Returns:
            Dictionary with chunks, DataFrame, and statistics
        """
        print(f"\n\n===== Testing {strategy} chunking strategy =====")
        
        # Chunk the document with this strategy
        chunks = self.document_service.chunk_document(self.converted_doc, chunking_strategy=strategy)
        
        # Convert to DataFrame
        df = self._chunks_to_dataframe(chunks)
        
        # Store results
        self.results[strategy] = {
            "chunks": chunks,
            "df": df,
            "stats": {
                "total_chunks": len(df),
                "avg_length": df['text_length'].mean(),
                "min_length": df['text_length'].min(),
                "max_length": df['text_length'].max()
            }
        }
        
        # Display samples
        print(f"\nSample chunks for {strategy} strategy:")
        samples = self._display_chunk_samples(df, n_samples=3)
        print(samples)
        
        # Print statistics
        print(f"Total chunks: {len(df)}")
        print(f"Average chunk length: {df['text_length'].mean():.1f} characters")
        print(f"Min chunk length: {df['text_length'].min()} characters")
        print(f"Max chunk length: {df['text_length'].max()} characters")
        
        return self.results[strategy]
    
    def run_all_strategies(self, strategies: Optional[List[str]] = None) -> Dict[str, Dict[str, Any]]:
        """Run all specified chunking strategies.
        
        Args:
            strategies: List of strategy names to run
            
        Returns:
            Dictionary with results for all strategies
        """
        if strategies is None:
            # Get available strategies from chunking service
            strategies = list(self.document_service.chunking_service.get_available_strategies().keys())
        
        for strategy in strategies:
            self.run_strategy(strategy)
        
        return self.results
    
    def compare_strategies(self) -> pd.DataFrame:
        """Compare statistics across all strategies.
        
        Returns:
            DataFrame with comparison of all strategies
        """
        if not self.results:
            print("No results to compare. Run strategies first.")
            return pd.DataFrame()
        
        comparison = []
        for strategy, result in self.results.items():
            stats = result["stats"]
            comparison.append({
                "strategy": strategy,
                "total_chunks": stats["total_chunks"],
                "avg_length": float(stats["avg_length"]),
                "min_length": int(stats["min_length"]),
                "max_length": int(stats["max_length"])
            })
        
        comparison_df = pd.DataFrame(comparison)
        return comparison_df
    
    def visualize_chunk_lengths(self, figsize: Tuple[int, int] = (12, 8)) -> None:
        """Visualize the distribution of chunk lengths for each strategy.
        
        Args:
            figsize: Figure size as (width, height) tuple
        """
        if not self.results:
            print("No results to visualize. Run strategies first.")
            return
        
        plt.figure(figsize=figsize)
        
        for strategy, result in self.results.items():
            df = result["df"]
            plt.hist(df["text_length"], alpha=0.5, bins=30, label=strategy)
        
        plt.title("Chunk Length Distribution by Strategy")
        plt.xlabel("Chunk Length (characters)")
        plt.ylabel("Frequency")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def save_results(self, output_dir: str = "data/chunking_results") -> None:
        """Save all results to disk.
        
        Args:
            output_dir: Directory to save results in
        """
        os.makedirs(output_dir, exist_ok=True)
        
        for strategy, result in self.results.items():
            # Save DataFrame
            result["df"].to_csv(f"{output_dir}/{strategy}_chunks.csv", index=False)
            
            # Save chunks
            with open(f"{output_dir}/{strategy}_chunks.pkl", 'wb') as f:
                pickle.dump(result["chunks"], f)
        
        # Save comparison
        comparison_df = self.compare_strategies()
        comparison_df.to_csv(f"{output_dir}/strategy_comparison.csv", index=False)
        
        print(f"✅ Saved all results to {output_dir}")
        
    def load_results(self, input_dir: str = "data/chunking_results") -> Dict[str, Dict[str, Any]]:
        """Load results from disk.
        
        Args:
            input_dir: Directory to load results from
            
        Returns:
            Dictionary with loaded results
        """
        strategies = [d.split("_chunks.csv")[0] for d in os.listdir(input_dir) 
                     if d.endswith("_chunks.csv")]
        
        for strategy in strategies:
            # Load DataFrame
            df_path = f"{input_dir}/{strategy}_chunks.csv"
            df = pd.read_csv(df_path)
            
            # Load chunks
            chunks_path = f"{input_dir}/{strategy}_chunks.pkl"
            with open(chunks_path, 'rb') as f:
                chunks = pickle.load(f)
            
            # Store in results
            self.results[strategy] = {
                "chunks": chunks,
                "df": df,
                "stats": {
                    "total_chunks": len(df),
                    "avg_length": df['text_length'].mean(),
                    "min_length": df['text_length'].min(),
                    "max_length": df['text_length'].max()
                }
            }
        
        print(f"✅ Loaded results for strategies: {', '.join(strategies)}")
        return self.results
    
    def insert_into_database(self, strategies: Optional[List[str]] = None) -> Dict[str, List[int]]:
        """Insert chunks from selected strategies into the database.
        
        Args:
            strategies: List of strategies to insert (None for all)
            
        Returns:
            Dictionary mapping strategies to lists of inserted chunk IDs
        """
        if not self.results:
            print("No results to insert. Run strategies first.")
            return {}
        
        if strategies is None:
            strategies = list(self.results.keys())
        
        # Connect to database
        conn = get_connection()
        inserted_ids = {}
        
        for strategy in strategies:
            if strategy not in self.results:
                print(f"Strategy '{strategy}' not found in results")
                continue
                
            print(f"\nInserting chunks for '{strategy}' strategy...")
            chunks = self.results[strategy]["chunks"]
            
            # Add embeddings to chunks
            print(f"Adding embeddings to {len(chunks)} chunks...")
            chunks_with_embeddings = self.document_service.get_embeddings_for_chunks(chunks)
            
            # Insert chunks into database
            try:
                print("Uploading chunks to database...")
                chunk_ids = bulk_validate_and_insert_chunks(conn, chunks_with_embeddings)
                inserted_ids[strategy] = chunk_ids
                print(f"✅ Successfully inserted {len(chunk_ids)} chunks with '{strategy}' strategy")
            except Exception as e:
                print(f"❌ Error inserting chunks: {e}")
                conn.rollback()
        
        # Close database connection
        conn.close()
        return inserted_ids
    
    def _chunks_to_dataframe(self, chunks: List[Dict[str, Any]]) -> pd.DataFrame:
        """Convert a list of chunks to a pandas DataFrame.
        
        Args:
            chunks: List of chunk dictionaries
            
        Returns:
            DataFrame with chunk data
        """
        # Extract metadata fields
        rows = []
        for i, chunk in enumerate(chunks):
            # Start with basic fields
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
                        row[f"meta_{key}"] = ", ".join(str(v) for v in value)
                    else:
                        row[f"meta_{key}"] = value
                
            rows.append(row)
        
        # Create DataFrame
        df = pd.DataFrame(rows)
        print(f"✅ Created DataFrame with {len(df)} chunks")
        return df
    
    def _display_chunk_samples(self, df: pd.DataFrame, n_samples: int = 5, 
                              text_preview_len: int = 200) -> pd.DataFrame:
        """Display sample chunks with truncated text.
        
        Args:
            df: DataFrame of chunks
            n_samples: Number of samples to display
            text_preview_len: Length of text preview
            
        Returns:
            DataFrame with samples
        """
        # Create a copy to avoid modifying the original
        preview_df = df.copy()
        
        # Truncate text for display
        preview_df["text_preview"] = preview_df["text"].str[:text_preview_len] + "..."
        
        # Select columns to display
        display_cols = ["chunk_id", "text_preview", "text_length"]
        
        # Add metadata columns
        metadata_cols = [col for col in preview_df.columns if col.startswith("meta_")]
        display_cols.extend(metadata_cols)
        
        # Get samples
        samples = preview_df[display_cols].sample(min(n_samples, len(df))).reset_index(drop=True)
        
        return samples 