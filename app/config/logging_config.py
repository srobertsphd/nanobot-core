"""
Logging Configuration Module

This module defines the logging configuration for the application using Python's
dictConfig. It sets up handlers, formatters, and filters for the root logger,
but provides utility functions to get non-root loggers for use in code.
"""

import logging.config
import sys
from typing import Dict, Any


def get_logging_config() -> Dict[str, Any]:
    """
    Returns the logging configuration dictionary for use with dictConfig.
    
    This configuration:
    - Sets up a console handler that writes to stdout
    - Configures the root logger with handlers and filters
    - Defines log formats and levels
    """
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "simple": {
                "format": "%(levelname)s - %(message)s",
            },
        },
        "filters": {
            # You can add custom filters here if needed
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "stream": sys.stdout,
            },
            # You can add file handlers or other handlers here if needed
        },
        "loggers": {
            # Empty on purpose - we don't configure specific loggers here
        },
        "root": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": True,
        },
    }


def configure_logging():
    """
    Configure logging for the application using dictConfig.
    
    This should be called once at application startup.
    """
    config = get_logging_config()
    logging.config.dictConfig(config)
    logging.info("Logging configured successfully") 