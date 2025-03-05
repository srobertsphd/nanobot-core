"""
Basic Logging Configuration

This module provides a simple logging setup that writes to console and file.
"""

import logging
import os
import sys

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # Console handler
        logging.StreamHandler(sys.stdout),
        # File handler
        logging.FileHandler("logs/app.log")
    ]
)

def get_logger(name):
    """Get a logger for a specific module."""
    return logging.getLogger(name) 