import streamlit as st
from app.database.std_sql_db import get_connection, search_similar_chunks
from app.services.openai_service import get_chat_response

# Test the function
if __name__ == "__main__":
    st.title("🤖 Nanobot POC")
    
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
            # Connect to the database
            conn = get_connection()
            try:
                # Use search_similar_chunks directly
                context_chunks = search_similar_chunks(conn, prompt, limit=5)
                print(f"Found {len(context_chunks)} relevant chunks")
            except Exception as e:
                print(f"Error retrieving context: {e}")
                context_chunks = []
            finally:
                conn.close()
        
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
        
        # Generate response using the context
        with st.spinner("Generating response..."):
            response = get_chat_response(prompt, context_chunks)
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
