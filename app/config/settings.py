"""
Application Settings Module

This module defines the configuration settings for the application using Pydantic.
It loads settings from environment variables and/or .env files, providing
type validation and default values.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from pathlib import Path

# Determine the project root directory (where the app directory is located)
PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()

class DatabaseSettings(BaseSettings):
    """Database connection settings for the application database.
    
    Loads configuration from environment variables with LOCAL_DB_ prefix.
    """
    name: str        # Database name
    user: str        # Database username
    password: str    # Database password
    host: str        # Database host address
    port: str        # Database port

    model_config = SettingsConfigDict(
        env_prefix="LOCAL_DB_"  # Looks for LOCAL_DB_NAME, LOCAL_DB_USER, etc.
    )

    def get_connection_dict(self) -> dict:
        """Returns a dictionary suitable for database connection libraries."""
        return {
            "dbname": self.name,
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port
        }

class AdminDatabaseSettings(BaseSettings):
    """Database connection settings for administrative operations.
    
    Loads configuration from environment variables with LOCAL_DB_ADMIN_ prefix.
    """
    name: str        # Admin database name
    user: str        # Admin database username
    password: str    # Admin database password
    host: str        # Admin database host address
    port: str        # Admin database port

    model_config = SettingsConfigDict(
        env_prefix="LOCAL_DB_ADMIN_"  # Looks for LOCAL_DB_ADMIN_NAME, etc.
    )

    def get_connection_dict(self) -> dict:
        """Returns a dictionary suitable for database connection libraries."""
        return {
            "dbname": self.name,
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port
        }

class NeonDatabaseSettings(BaseSettings):
    """Neon database connection settings.
    
    Uses a connection URL from the NEON_DB_URL environment variable.
    """
    db_url: str  # Full connection URL for Neon

    model_config = SettingsConfigDict(
        env_prefix="NEON_"  # Looks for NEON_DB_URL
    )

class OpenAISettings(BaseSettings):
    """OpenAI API configuration settings.
    
    Loads configuration from environment variables with OPENAI_ prefix.
    """
    api_key: str                         # OpenAI API key
    model: str = "gpt-4o"                # Default model for chat completions
    embedding_model: str = "text-embedding-3-small"  # Model for embeddings
    temperature: float = 0.0             # Controls randomness (0=deterministic, 1=creative)
    chat_max_tokens: Optional[int] = None          # Maximum tokens in model's response
    embedding_max_tokens: int = 8191     # Maximum tokens for text embeddings
    embedding_dimensions: int = 1536  # Dimensions for this model

    model_config = SettingsConfigDict(
        env_prefix="OPENAI_"  # Looks for OPENAI_API_KEY, etc.
    )

class VectorIndexSettings(BaseSettings):
    """Vector index settings for PostgreSQL PG vector extension."""
    
    # Index type: 'hnsw' or 'ivfflat'
    index_type: str = "hnsw" # HNSW is what is needed to have vectors over 2000 dimensions.
    
    # HNSW parameters
    hnsw_m: int = 32  # Higher value (32) for better search quality
    hnsw_ef_construction: int = 100  # Higher value (100) for better search quality
    
    # IVFFlat parameters (if needed)
    ivfflat_lists: int = 100
    
    model_config = SettingsConfigDict(
        env_prefix="VECTOR_INDEX_"
    )

class LogfireSettings(BaseSettings):
    """Logfire configuration settings.
    
    Loads configuration from environment variables with LOGFIRE_ prefix.
    """
    token: Optional[str] = None  # Make token optional with default None

    model_config = SettingsConfigDict(
        env_prefix="LOGFIRE_"  # This will look for LOGFIRE_TOKEN
    )

class FilePathSettings(BaseSettings):
    """File path settings for data storage.
    
    Configures paths for document storage, processing and chunking.
    """
    # Base data directory (relative to project root)
    base_dir: str = "data"
    
    # Subdirectories
    original_docs_dir: str = "original_docs"
    converted_docs_dir: str = "converted_docs"
    chunking_results_dir: str = "chunking_results"
    
    model_config = SettingsConfigDict(
        env_prefix="DATA_"  # Looks for DATA_BASE_DIR, DATA_ORIGINAL_DOCS_DIR, etc.
    )
    
    def get_base_dir_path(self) -> Path:
        """Returns the absolute path to the base data directory."""
        return PROJECT_ROOT / self.base_dir
    
    def get_original_docs_path(self) -> Path:
        """Returns the path to the original documents directory."""
        return self.get_base_dir_path() / self.original_docs_dir
    
    def get_converted_docs_path(self) -> Path:
        """Returns the path to the converted documents directory."""
        return self.get_base_dir_path() / self.converted_docs_dir
    
    def get_chunking_results_path(self) -> Path:
        """Returns the path to the chunking results directory."""
        return self.get_base_dir_path() / self.chunking_results_dir
    
    def create_directories(self) -> None:
        """Creates all required data directories if they don't exist."""
        for path in [
            self.get_base_dir_path(),
            self.get_original_docs_path(),
            self.get_converted_docs_path(),
            self.get_chunking_results_path()
        ]:
            path.mkdir(parents=True, exist_ok=True)

class Settings(BaseSettings):
    """Main application settings container.
    
    Aggregates all sub-settings and loads from .env file.
    """
    local_db: DatabaseSettings = DatabaseSettings()
    admin_db: AdminDatabaseSettings = AdminDatabaseSettings()
    neon_db: NeonDatabaseSettings = NeonDatabaseSettings()
    openai: OpenAISettings = OpenAISettings()
    vector_index: VectorIndexSettings = VectorIndexSettings()
    logfire: LogfireSettings = LogfireSettings()
    file_paths: FilePathSettings = FilePathSettings()
    
    # Flag to determine which database to use (from USE_NEON environment variable)
    use_neon: bool = False  # Default value ONLY if USE_NEON is not set in .env

    model_config = SettingsConfigDict(
        env_file=".env",                # Load from .env file
        env_file_encoding="utf-8",      # Encoding for .env file
        case_sensitive=False,           # Case-insensitive env vars
        extra='ignore'                  # Ignore extra env vars
    )
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create directories during initialization
        self.file_paths.create_directories()

# Create a singleton instance for global access
settings = Settings()

def reload_settings():
    """Reload settings from environment variables."""
    global settings
    settings = Settings()
    settings.file_paths.create_directories()
    return settings