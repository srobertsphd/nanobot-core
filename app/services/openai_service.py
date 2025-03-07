"""
OpenAI Service Module

This module provides a centralized interface for all OpenAI API calls,
including chat completions and embeddings.
"""

import logging
import logfire
from app.config.settings import settings
from app.services.prompt_loader import PromptLoader
from openai import OpenAI

# set up dedicated logger for the openai service
logger = logging.getLogger(__name__)

# Initialize the OpenAI client
client = OpenAI(api_key=settings.openai.api_key)

# You can use both approaches: instrument the client for automatic tracing
# AND use decorators for additional context
logfire.instrument_openai(client)

@logfire.instrument("openai.embedding", extract_args=True)
def get_embedding(text, model=None) -> list[float]:
    """Get embedding for text using OpenAI API."""
    # Use the model from settings if not specified
    if model is None:
        model = settings.openai.embedding_model
    
    # Log the request
    logger.info(f"Generating embedding with model {model}")
    
    # Call OpenAI API - this will be automatically traced by Logfire
    response = client.embeddings.create(
        input=text,
        model=model
    )
    
    # Process the response
    embedding = response.data[0].embedding
    embedding = [float(x) for x in embedding]
     
    # Log the result
    logger.info(f"Generated embedding with {len(embedding)} dimensions")
    
    return embedding

@logfire.instrument("openai.chat_completion", extract_args=True)
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
    
    # Log the request
    logger.info(f"Generating chat completion for prompt: '{prompt[:50]}...'")
    
    try:
        # Call OpenAI API - this will be automatically traced by Logfire
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
        
        # Log the result
        logger.info("Chat completion successful")
        
        return response.choices[0].message.content
    except Exception as e:
        # Log the error
        logger.error(f"Error generating chat completion: {str(e)}")
        return f"Sorry, I encountered an error while generating a response: {str(e)}" 