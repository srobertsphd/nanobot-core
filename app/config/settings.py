from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseSettings(BaseSettings):
    name: str
    user: str
    password: str
    host: str
    port: str

    model_config = SettingsConfigDict(
        env_prefix="LOCAL_DB_"  # This will look for LOCAL_DB_NAME, LOCAL_DB_USER, etc.
    )

    def get_connection_dict(self) -> dict:
        return {
            "dbname": self.name,
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port
        }

class AdminDatabaseSettings(BaseSettings):
    name: str
    user: str
    password: str
    host: str
    port: str

    model_config = SettingsConfigDict(
        env_prefix="LOCAL_DB_ADMIN_"  # This will look for LOCAL_DB_ADMIN_NAME, etc.
    )

    def get_connection_dict(self) -> dict:
        return {
            "dbname": self.name,
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port
        }

class OpenAISettings(BaseSettings):
    api_key: str
    model: str = "gpt-4o"
    embedding_model: str = "text-embedding-3-large"
    temperature: float = 0.0
    chat_max_tokens: int = 4096  # Maximum tokens in the model's response for chat completions
    embedding_max_tokens: int = 8191  # Maximum tokens for text that can be embedded

    model_config = SettingsConfigDict(
        env_prefix="OPENAI_"  # This will look for OPENAI_API_KEY, etc.
    )

class Settings(BaseSettings):
    local_db: DatabaseSettings = DatabaseSettings()
    admin_db: AdminDatabaseSettings = AdminDatabaseSettings()
    openai: OpenAISettings = OpenAISettings()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra='ignore'
    )

# Create a singleton instance
settings = Settings()