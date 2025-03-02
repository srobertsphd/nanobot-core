import streamlit as st
from openai import OpenAI
from app.database.std_sql_db import get_connection, search_similar_chunks


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
    
    # Connect to the database
    conn = get_connection()
    
    try:
        # Use the existing search_similar_chunks function
        context_chunks = search_similar_chunks(conn, query, limit)
        
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
        
        # Display context information
        st.info(f"Found {len(context_chunks)} relevant chunks of information")
        
        # Display context details (expandable)
        with st.expander("View retrieved context", expanded=False):
            if context_chunks:
                for i, chunk in enumerate(context_chunks):
                    st.markdown(f"**Chunk {i+1}** (Similarity: {chunk['similarity']:.4f})")
                    st.markdown(f"```\n{chunk['text']}\n```")
                    
                    # Display metadata in a more readable format
                    if 'metadata' in chunk:
                        metadata = chunk['metadata']
                        st.markdown("**Metadata:**")
                        for key, value in metadata.items():
                            st.markdown(f"- **{key}**: {value}")
                    
                    # Add a separator between chunks
                    if i < len(context_chunks) - 1:
                        st.divider()
            else:
                st.warning("No relevant information found in the database.")
        
        # TODO: Next step will be to implement get_chat_response function
        # that uses this context to generate a response
        
        # For now, just acknowledge the query
        with st.chat_message("assistant"):
            response = f"I found {len(context_chunks)} relevant pieces of information in the database."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
