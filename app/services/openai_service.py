"""
OpenAI Service Module

This module provides a centralized interface for all OpenAI API calls,
including chat completions and embeddings.
"""

from openai import OpenAI
import jinja2
from app.config.settings import settings
from app.services.prompt_loader import PromptLoader

# Initialize the OpenAI client
client = OpenAI(api_key=settings.openai.api_key)

# Set up Jinja2 environment for templates
template_loader = jinja2.FileSystemLoader(searchpath="app/prompts/templates")
template_env = jinja2.Environment(loader=template_loader)

def get_embedding(text, model=None) -> list[float]:
    """Get embedding for text using OpenAI API."""
    # Use the model from settings if not specified
    if model is None:
        model = settings.openai.embedding_model
        
    response = client.embeddings.create(
        input=text,
        model=model
    )
    embedding = response.data[0].embedding
    
    # Make sure the embedding is in the correct format for pgvector
    # It should be a list of floats, not a numpy array or other format
    embedding = [float(x) for x in embedding]
    
    return embedding

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
    
    # Get system instructions from existing template
    system_message = PromptLoader.render_prompt("rag_system_prompt")
    
    try:
        # Call OpenAI API using settings from config
        response = client.chat.completions.create(
            model=settings.openai.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": f"Here's relevant information I found:\n\n{context_text}"}
            ],
            temperature=settings.openai.temperature,
            max_tokens=settings.openai.chat_max_tokens
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Sorry, I encountered an error while generating a response: {str(e)}" 