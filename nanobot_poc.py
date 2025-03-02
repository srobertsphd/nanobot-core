import streamlit as st
from openai import OpenAI
from app.database.std_sql_db import get_connection, search_similar_chunks
import jinja2
from app.config.settings import settings

client = OpenAI()

# Set up Jinja2 environment
template_loader = jinja2.FileSystemLoader(searchpath="app/prompts/templates")
template_env = jinja2.Environment(loader=template_loader)

def get_chat_response(prompt: str, context_chunks: list) -> str:
    """
    Generate a response using OpenAI's chat completion API with retrieved context
    
    Args:
        prompt: The user's question
        context_chunks: List of relevant chunks from the database
        
    Returns:
        Generated response from the model
    """
    # Prepare context text from chunks
    context_text = ""
    for chunk in context_chunks:
        context_text += f"{chunk['text']}\n\n"
        if 'metadata' in chunk:
            context_text += f"Source: {chunk['metadata'].get('source', 'Unknown')}\n\n"
    
    # Load and render the system prompt template
    template = template_env.get_template("rag_system_prompt.j2")
    system_message = template.render(context_text=context_text)
    
    try:
        # Print the model being used
        print(f"Using model: {settings.openai.model}")
        
        # Call OpenAI API using settings from config
        response = client.chat.completions.create(
            model=settings.openai.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=settings.openai.temperature,
            max_tokens=settings.openai.chat_max_tokens
        )
        
        # Extract and return the response text
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Sorry, I encountered an error while generating a response: {str(e)}"

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
