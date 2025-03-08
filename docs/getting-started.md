# Getting Started with NanoBot

This guide will help you set up and start using NanoBot.

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL with pgvector extension
- OpenAI API key

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nanobot-poc.git
   cd nanobot-poc
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   LOCAL_DB_NAME=nanobot
   LOCAL_DB_USER=postgres
   LOCAL_DB_PASSWORD=your_password
   LOCAL_DB_HOST=localhost
   LOCAL_DB_PORT=5432
   LOGFIRE_TOKEN=your_logfire_token
   ```

5. Initialize the database:
   ```bash
   python -m app.database.db_setup
   ```

## Running the Application

Start the Streamlit web interface:

```bash
streamlit run nanobot_poc.py
```

This will open a web browser with the NanoBot interface.
