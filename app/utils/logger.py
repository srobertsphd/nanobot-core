"""
Logger Utility Module

This module provides utility functions for getting loggers in your code.
It ensures that you don't use the root logger directly, but instead get
named loggers for specific modules or components.
"""

import logging
from app.config.logging_config import configure_logging

# Initialize logging configuration when this module is imported
# configure_logging()


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger for a specific module or component.
    
    Args:
        name: The name of the logger, typically __name__ from the calling module
        
    Returns:
        A configured logger instance
        
    Example:
        ```python
        from app.utils.logger import get_logger
        
        # In a module
        logger = get_logger(__name__)
        logger.info("This is an info message")
        logger.error("This is an error message")
        ```
    """
    return logging.getLogger(name)


# Example usage in this module
logger = get_logger(__name__)