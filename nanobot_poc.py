import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from app.database.std_sql_db import get_connection
from app.utils.openai_embedding import get_embedding
# import json
import psycopg2.extras

load_dotenv()

client = OpenAI()

def get_context_from_db(query: str, limit: int = 5):
    """
    Get relevant context from the database based on the query
    
    Args:
        query: The user's question
        limit: Maximum number of chunks to retrieve
        
    Returns:
        List of relevant chunks with text, metadata, and similarity score
    """
    print(f"Searching for context related to: {query}")
    
    # Get embedding for the query
    query_embedding = get_embedding(query)
    
    # Connect to the database
    conn = get_connection()
    
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # Search for similar chunks using cosine similarity
            search_query = """
                SELECT 
                    text,
                    metadata,
                    1 - (vector <=> %s::vector) as similarity
                FROM chunks
                WHERE 1 - (vector <=> %s::vector) > 0.7  -- Similarity threshold
                ORDER BY similarity DESC
                LIMIT %s;
            """
            cur.execute(search_query, (query_embedding, query_embedding, limit))
            results = cur.fetchall()
            
            # Format results
            context_chunks = []
            for row in results:
                # Parse metadata from JSONB if needed
                metadata = row['metadata']
                
                chunk = {
                    "text": row['text'],
                    "metadata": metadata,
                    "similarity": row['similarity']
                }
                context_chunks.append(chunk)
            
            print(f"Found {len(context_chunks)} relevant chunks")
            return context_chunks
    except Exception as e:
        print(f"Error retrieving context: {e}")
        return []
    finally:
        conn.close()

# Test the function
if __name__ == "__main__":
    st.title("Nanobot POC")
    
    # Simple chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Get user input
    if prompt := st.chat_input("What would you like to know?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get context from database
        with st.spinner("Searching knowledge base..."):
            context_chunks = get_context_from_db(prompt)
        
        # Display context (for debugging)
        if st.checkbox("Show retrieved context"):
            st.write(context_chunks)
        
        # TODO: Next step will be to implement get_chat_response function
        # that uses this context to generate a response
        
        # For now, just acknowledge the query
        with st.chat_message("assistant"):
            response = f"I found {len(context_chunks)} relevant pieces of information in the database."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
