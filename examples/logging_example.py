#!/usr/bin/env python
"""
Logging Example

This script demonstrates how to use the logging configuration in your code.
Run it directly to see logging in action.
"""
import logging
from app.services.openai_service import get_embedding, get_chat_response
import time
from app.utils.logger import get_logger
from app.config.logging_config import configure_logging

configure_logging()
logger = get_logger(__name__)




def demonstrate_logging():
    """
    Demonstrate different logging levels and messages.
    """
    logger.debug("This is a debug message - only shown if log level is DEBUG or lower")
    logger.info("This is an info message - shown if log level is INFO or lower")
    logger.warning("This is a warning message - shown if log level is WARNING or lower")
    logger.error("This is an error message - shown if log level is ERROR or lower")
    logger.critical("This is a critical message - shown if log level is CRITICAL or lower")
    
    # You can also include variables in log messages
    user_id = "user123"
    action = "login"
    logger.info(f"User {user_id} performed action: {action}")
    
    # For more complex formatting or expensive operations, use this pattern
    # to avoid the overhead if the log level is not enabled
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(f"Expensive operation result: {calculate_expensive_result()}")
    
    # You can also include exception information
    try:
        result = 1 / 0  # noqa: F841
    except Exception as e:  # noqa: F841
        logger.exception("An error occurred during calculation")
        # The exception() method automatically includes the traceback
    
    # Demonstrate using extra attributes
    logger.info(
        "User performed an action",
        extra={
            "user_id": "user456",
            "action": "checkout",
            "cart_value": 125.99,
            "items_count": 3,
            "customer_type": "premium"
        }
    )
    
    # Demonstrate using extra with different log levels
    logger.debug(
        "API request details", 
        extra={
            "endpoint": "/api/products",
            "method": "GET",
            "response_time_ms": 45,
            "status_code": 200
        }
    )
    
    logger.warning(
        "Rate limit approaching",
        extra={
            "current_rate": 95,
            "limit": 100,
            "client_ip": "192.168.1.1",
            "endpoint": "/api/search"
        }
    )
    
    logger.error(
        "Database connection failed",
        extra={
            "db_host": "db.example.com",
            "retry_count": 3,
            "error_code": "CONN_REFUSED"
        }
    )


def demonstrate_openai_logging():
    """
    Demonstrate logging with OpenAI API calls.
    """
    logger.info("Starting OpenAI API logging demonstration")
    
    # Test embedding
    text = "This is a test of the OpenAI embedding service with Logfire logging."
    logger.info(f"Generating embedding for text: '{text[:30]}...'")
    
    start_time = time.time()
    embedding = get_embedding(text)
    duration = time.time() - start_time
    
    logger.info(
        f"Generated embedding with {len(embedding)} dimensions",
        extra={
            "embedding_dimensions": len(embedding),
            "text_length": len(text),
            "duration_seconds": duration
        }
    )
    
    # Test chat completion
    prompt = "What is the capital of France?"
    context_chunks = [{"text": "Paris is the capital of France.", "metadata": {"source": "test"}}]
    
    logger.info(f"Generating chat completion for prompt: '{prompt}'")
    
    start_time = time.time()
    response = get_chat_response(prompt, context_chunks)
    duration = time.time() - start_time
    
    logger.info(
        f"Received response: '{response[:50]}...'",
        extra={
            "prompt": prompt,
            "response_length": len(response),
            "duration_seconds": duration,
            "context_chunks_count": len(context_chunks)
        }
    )
    
    return {
        "embedding_dimensions": len(embedding),
        "response": response
    }


def calculate_expensive_result():
    """Simulate an expensive calculation."""
    return {
        "value": sum(i * i for i in range(1000)),
        "computation_time": time.time()
    }


def run_all_examples():
    """Run all logging examples."""
    print("\n=== Basic Logging Examples ===")
    demonstrate_logging()
    
    print("\n=== OpenAI API Logging Examples ===")
    result = demonstrate_openai_logging()
    print(f"Generated embedding with {result['embedding_dimensions']} dimensions")
    print(f"Response: {result['response']}")


if __name__ == "__main__":
    print("Running logging examples...")
    run_all_examples()
    print("\nLogging examples complete!")
