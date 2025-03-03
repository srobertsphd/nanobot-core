"""
Application Settings Module

This module defines the configuration settings for the application using Pydantic.
It loads settings from environment variables and/or .env files, providing
type validation and default values.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

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

class OpenAISettings(BaseSettings):
    """OpenAI API configuration settings.
    
    Loads configuration from environment variables with OPENAI_ prefix.
    """
    api_key: str                         # OpenAI API key
    model: str = "gpt-4o"                # Default model for chat completions
    embedding_model: str = "text-embedding-3-large"  # Model for embeddings
    temperature: float = 0.0             # Controls randomness (0=deterministic, 1=creative)
    chat_max_tokens: Optional[int] = None          # Maximum tokens in model's response
    embedding_max_tokens: int = 8191     # Maximum tokens for text embeddings

    model_config = SettingsConfigDict(
        env_prefix="OPENAI_"  # Looks for OPENAI_API_KEY, etc.
    )

class Settings(BaseSettings):
    """Main application settings container.
    
    Aggregates all sub-settings and loads from .env file.
    """
    local_db: DatabaseSettings = DatabaseSettings()
    admin_db: AdminDatabaseSettings = AdminDatabaseSettings()
    openai: OpenAISettings = OpenAISettings()

    model_config = SettingsConfigDict(
        env_file=".env",                # Load from .env file
        env_file_encoding="utf-8",      # Encoding for .env file
        case_sensitive=False,           # Case-insensitive env vars
        extra='ignore'                  # Ignore extra env vars
    )

# Create a singleton instance for global access
settings = Settings()