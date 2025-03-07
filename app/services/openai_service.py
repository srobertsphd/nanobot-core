"""
OpenAI Service Module

This module provides a centralized interface for all OpenAI API calls,
including chat completions and embeddings.
"""

import logging
import time
from app.config.settings import settings
from app.services.prompt_loader import PromptLoader
from openai import OpenAI

# set up dedicated logger for the openai service
logger = logging.getLogger(__name__)
# Initialize the OpenAI client
client = OpenAI(api_key=settings.openai.api_key)

def get_embedding(text, model=None) -> list[float]:
    """Get embedding for text using OpenAI API."""
    # Use the model from settings if not specified
    if model is None:
        model = settings.openai.embedding_model
    
    start_time = time.time()
    request_id = f"emb_{int(start_time * 1000)}"
    
    logger.info(f"Starting embedding request {request_id}", extra={
        "request_id": request_id,
        "model": model,
        "text_length": len(text),
        "operation": "embedding"
    })
    
    try:
        response = client.embeddings.create(
            input=text,
            model=model
        )
        embedding = response.data[0].embedding
        
        # Make sure the embedding is in the correct format for pgvector
        # It should be a list of floats, not a numpy array or other format
        embedding = [float(x) for x in embedding]
        
        # Calculate duration
        duration = time.time() - start_time
        
        # Log success
        logger.info(f"Embedding request {request_id} completed successfully", extra={
            "request_id": request_id,
            "model": model,
            "duration_seconds": duration,
            "embedding_dimensions": len(embedding),
            "operation": "embedding",
            "status": "success"
        })
        
        return embedding
    except Exception as e:
        # Calculate duration
        duration = time.time() - start_time
        
        # Log error
        logger.error(f"Embedding request {request_id} failed: {str(e)}", extra={
            "request_id": request_id,
            "model": model,
            "duration_seconds": duration,
            "error": str(e),
            "operation": "embedding",
            "status": "error"
        })
        raise

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
    
    # Generate a unique request ID
    start_time = time.time()
    request_id = f"chat_{int(start_time * 1000)}"
    
    # Log the start of the request
    logger.info(f"Starting chat completion request {request_id}", extra={
        "request_id": request_id,
        "model": settings.openai.model,
        "prompt_length": len(prompt),
        "context_chunks": len(context_chunks),
        "temperature": settings.openai.temperature,
        "max_tokens": settings.openai.chat_max_tokens,
        "operation": "chat_completion"
    })
    
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
        
        # Calculate duration
        duration = time.time() - start_time
        
        # Log success
        logger.info(f"Chat completion request {request_id} completed successfully", extra={
            "request_id": request_id,
            "model": settings.openai.model,
            "duration_seconds": duration,
            "completion_tokens": response.usage.completion_tokens,
            "prompt_tokens": response.usage.prompt_tokens,
            "total_tokens": response.usage.total_tokens,
            "operation": "chat_completion",
            "status": "success"
        })
        
        return response.choices[0].message.content
    except Exception as e:
        # Calculate duration
        duration = time.time() - start_time
        
        # Log error
        logger.error(f"Chat completion request {request_id} failed: {str(e)}", extra={
            "request_id": request_id,
            "model": settings.openai.model,
            "duration_seconds": duration,
            "error": str(e),
            "operation": "chat_completion",
            "status": "error"
        })
        
        return f"Sorry, I encountered an error while generating a response: {str(e)}" 