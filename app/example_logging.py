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


def calculate_expensive_result():
    """Simulate an expensive calculation."""
    return sum(i * i for i in range(1000000))


if __name__ == "__main__":
    demonstrate_logging() 