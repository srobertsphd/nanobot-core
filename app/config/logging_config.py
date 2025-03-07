"""
Logging Configuration Module

This module defines the logging configuration for the application using Python's
dictConfig. It sets up handlers, formatters, and filters for the root logger,
but provides utility functions to get non-root loggers for use in code.
"""

import logging.config
import logging.handlers
import logfire
import sys
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
                "datefmt": "%Y-%m-%dT%H:%M:%S%z",  # ISO-8601 format with timezone
            },
            "simple": {
                "format": "%(levelname)s: %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S%z"
            },
            "json": {
                "()": "app.utils.json_formatter.MyJSONFormatter",
                "fmt_keys": {
                    "level": "levelname",
                    "message": "message",
                    "timestamp": "timestamp",
                    "logger": "name",
                    "module": "module",
                    "function": "funcName",
                    "line": "lineno",
                    "thread_name": "threadName"
                }
            },
        },
        "filters": {
            # You can add custom filters here if needed
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "WARNING",
                "formatter": "standard",
                "stream": sys.stdout,
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "filename": "logs/app.log",
                "maxBytes": 1048576,
                "backupCount": 3,
            },
            "json_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "json",
                "filename": "logs/app.json.log",
                "maxBytes": 1048576,
                "backupCount": 3,
            },
            "logfire": {
                "class": "logfire.LogfireLoggingHandler",
                "level": "WARNING",
                "formatter": "json",
            },
        },
        "loggers": {
            # Empty on purpose - we don't configure specific loggers here
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console", "file", "json_file", "logfire"],
            "propagate": True,
        },
    }


def configure_logging():
    """
    Configure logging for the application using dictConfig.
    """
    # Get the logging config first
    config = get_logging_config()
    
    # Get Logfire token directly from environment
    from app.config.settings import reload_settings
    # HACK eload settings to get the Logfire token -- I DONT KNOW WHY THIS IS NEEDED
    settings = reload_settings()
    logfire_token = settings.logfire.token #os.environ.get('LOGFIRE_TOKEN')
    
    # Configure Logfire if token is available
    if logfire_token:
        print(f"Configuring Logfire with token: {logfire_token[:5]}...")
        try:
            logfire.configure(token=logfire_token)
        except Exception as e:
            print(f"Warning: Logfire configuration failed: {e}")
            if "logfire" in config["root"]["handlers"]:
                config["root"]["handlers"].remove("logfire")
    else:
        print("No Logfire token found in environment variables")
        # Remove Logfire handler if no token
        if "logfire" in config["root"]["handlers"]:
            config["root"]["handlers"].remove("logfire")
    
    # Set up logging
    logging.config.dictConfig(config)
    logging.info("Logging configured successfully") 