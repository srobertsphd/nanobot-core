"""
Common Database Constants and Utilities

This module provides shared constants, queries, and utility functions
used across all database modules.
"""

import psycopg2
import psycopg2.extras
from app.config.settings import settings


def get_connection(use_neon=None) -> psycopg2.connect:
    """
    Connect to the PostgreSQL database using settings configuration.
    gives the option to override the settings.use_neon flag
    
    Args:
        use_neon (bool, optional): Override settings.use_neon flag.
            If None, uses the value from settings.use_neon.
    
    Returns:
        psycopg2.connect: Database connection
        
    Raises:
        psycopg2.Error: If connection fails
    """
    try:
        # Determine whether to use Neon
        if use_neon is None:
            use_neon = settings.use_neon
            
        if use_neon:
            # Connect to Neon using URL
            conn = psycopg2.connect(settings.neon_db.db_url)
            print("Connected to Neon database")
        else:
            # Connect to local database using connection parameters
            conn = psycopg2.connect(**settings.local_db.get_connection_dict())
            print("Connected to local database")
            
        return conn
    except psycopg2.Error as e:
        db_type = "Neon" if use_neon else "local"
        print(f"Error connecting to {db_type} database: {e}")
        raise 