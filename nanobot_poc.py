import streamlit as st
from app.database.db_common import get_connection
from app.database.db_retrieval import search_similar_chunks_with_filters
from app.services.openai_service import get_chat_response
from app.services.retrieval_service import get_chunking_strategies, get_filenames

# Test the function
if __name__ == "__main__":
    st.title("🤖 Nanobot POC")
    
    # Setup sidebar
    with st.sidebar:
        st.header("Retrieval Configuration")
        
        # Connect to the database to get metadata options
        conn = get_connection()
        try:
            chunking_strategies = get_chunking_strategies(conn)
            filenames = get_filenames(conn)
            
            if not chunking_strategies:
                st.error("No chunking strategies found in the database")
                chunking_strategies = ["default"]
                
            if not filenames:
                st.warning("No files found in the database")
                filenames = []
        except Exception as e:
            st.error(f"Error loading metadata options: {e}")
            chunking_strategies = ["default"]
            filenames = []
        finally:
            conn.close()
        
        # Number of chunks to retrieve
        num_chunks = st.slider(
            "Number of chunks to retrieve", 
            min_value=1, 
            max_value=10, 
            value=5,
            step=1
        )
        
        # Chunking strategy selector (required)
        chunking_strategy = st.selectbox(
            "Chunking Strategy (required)",
            options=chunking_strategies,
            index=0,
            key="chunking_strategy"
        )
        
        # Filename multi-selector
        st.write("Source Files (select at least one or 'All Files')")
        all_files = st.checkbox("All Files", value=True, key="all_files")
        
        selected_files = []
        if not all_files:
            # Only show the multi-select if "All Files" is not checked
            if filenames:
                selected_files = st.multiselect(
                    "Select specific files",
                    options=filenames,
                    default=[filenames[0]] if filenames else None,
                    key="selected_files"
                )
                
                # Validate at least one file is selected
                if not selected_files:
                    st.error("Please select at least one file or choose 'All Files'")
            else:
                st.error("No files available to select")
    
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
        
        # Validate file selection
        if not all_files and not selected_files:
            with st.chat_message("assistant"):
                error_msg = "Please select at least one file or choose 'All Files' in the sidebar."
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
            st.stop()
        
        # Get context from database
        with st.spinner("Searching knowledge base..."):
            # Connect to the database
            conn = get_connection()
            try:
                # Use the filtered search function with the sidebar configuration
                if all_files:
                    # Search across all files
                    context_chunks = search_similar_chunks_with_filters(
                        conn, 
                        prompt, 
                        limit=num_chunks,
                        chunking_strategy=chunking_strategy,
                        filename=None  # None means all files
                    )
                else:
                    # Search in multiple specific files
                    all_chunks = []
                    for file in selected_files:
                        file_chunks = search_similar_chunks_with_filters(
                            conn, 
                            prompt, 
                            limit=num_chunks,
                            chunking_strategy=chunking_strategy,
                            filename=file
                        )
                        all_chunks.extend(file_chunks)
                    
                    # Sort combined results by similarity and limit to num_chunks
                    context_chunks = sorted(all_chunks, key=lambda x: x['similarity'], reverse=True)[:num_chunks]
                
                print(f"Found {len(context_chunks)} relevant chunks")
            except Exception as e:
                print(f"Error retrieving context: {e}")
                st.error(f"Error retrieving context: {e}")
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
