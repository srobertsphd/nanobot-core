import streamlit as st
from app.config.logging_config import configure_logging
from app.utils.logger import get_logger

# ------------------------------------------------------------
# initialize logging before other imports that call the logger
# ------------------------------------------------------------

if "logging_initialized" not in st.session_state:
    configure_logging()  # Only logging (including Logfire handler)
    st.session_state["logging_initialized"] = True
    
logger = get_logger(__name__)

# ------------------------------------------------------------
# ------------------------------------------------------------

from app.database.common import get_connection  # noqa: E402
from app.database.retrieval import search_similar_chunks_with_filters, get_chunking_strategies, get_filenames  # noqa: E402
from app.services.openai_service import get_chat_response  # noqa: E402

if "logging_initialized" not in st.session_state:
    configure_logging()  # Only logging (including Logfire handler)
    st.session_state["logging_initialized"] = True
    
logger = get_logger(__name__)

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
            all_filenames = get_filenames(conn)
            
            # Get mapping of strategies to filenames
            strategy_to_files = {}
            for strategy in chunking_strategies:
                # Query to get filenames for this strategy
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT DISTINCT metadata->>'filename' 
                        FROM chunks 
                        WHERE metadata->>'chunking_strategy' = %s
                        ORDER BY metadata->>'filename'
                    """, (strategy,))
                    strategy_files = [row[0] for row in cur.fetchall()]
                    strategy_to_files[strategy] = strategy_files
            
            if not chunking_strategies:
                st.error("No chunking strategies found in the database")
                chunking_strategies = ["default"]
                strategy_to_files = {"default": []}
                
            if not all_filenames:
                st.warning("No files found in the database")
                all_filenames = []
        except Exception as e:
            st.error(f"Error loading metadata options: {e}")
            chunking_strategies = ["default"]
            all_filenames = []
            strategy_to_files = {"default": []}
        finally:
            conn.close()
        
        # Number of chunks to retrieve
        num_chunks = st.slider(
            "Number of chunks to retrieve", 
            min_value=1, 
            max_value=10, 
            value=3,
            step=1
        )
        
        # Chunking strategy selector (required) - set default as starting strategy
        default_index = 0
        if "default" in chunking_strategies:
            default_index = chunking_strategies.index("default")
        
        chunking_strategy = st.selectbox(
            "Chunking Strategy",
            options=chunking_strategies,
            index=default_index,
            key="chunking_strategy"
        )
        
        # Get files available for this strategy
        available_files = strategy_to_files.get(chunking_strategy, [])
        
        # File selector - start with empty selection
        if available_files:
            selected_files = st.multiselect(
                "Select documents to search",
                options=available_files,
                default=[],  # Start with empty selection
                key="selected_files"
            )
            
            # Validate at least one file is selected
            if not selected_files:
                st.error("Please select at least one document")
        else:
            st.error(f"No documents available with '{chunking_strategy}' strategy")
            selected_files = []
    
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
        if not selected_files:
            with st.chat_message("assistant"):
                error_msg = "Please select at least one document in the sidebar."
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
            st.stop()
        
        # Get context from database
        with st.spinner("Searching knowledge base..."):
            # Connect to the database
            conn = get_connection()
            try:
                # Search in selected files
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


