import os
from dotenv import load_dotenv

# Load environment variables from.env file
load_dotenv()

# configure for OpenAi API usage
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")
# COMPLETION_MODEL = os.getenv("OPENAI_COMPLETION_MODEL")

# Configure for Neon database API
# DATABASE_URL = os.getenv("DEVELOPMENT_DB_URL")
# SQL_DB_BRANCH_URL = os.getenv("DEVELOPMENT_SQL_DB_URL")