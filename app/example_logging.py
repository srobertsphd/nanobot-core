"""
Example Logging Usage

This module demonstrates how to use the logging configuration in your code.
"""

from app.utils.logger import get_logger
import logging

# Get a logger for this module
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
        result = 1 / 0
    except Exception as e:
        logger.exception("An error occurred during calculation")
        # The exception() method automatically includes the traceback


def calculate_expensive_result():
    """Simulate an expensive calculation."""
    return sum(i * i for i in range(1000000))


if __name__ == "__main__":
    demonstrate_logging() 