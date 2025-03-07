"""
JSON Formatter for Logging

This module provides a custom JSON formatter for structured logging.
"""

import json
import logging
import datetime
from typing import Dict, Any, Optional
try:
    from typing import override
except ImportError:
    from typing_extensions import override


class MyJSONFormatter(logging.Formatter):
    """
    Custom formatter that outputs log records as JSON objects.
    
    Allows customization of field names through fmt_keys parameter.
    """
    
    def __init__(self, fmt_keys: Optional[Dict[str, str]] = None):
        """
        Initialize the formatter with custom field mappings.
        
        Args:
            fmt_keys: Dictionary mapping output keys to record attributes
        """
        super().__init__()
        self.fmt_keys = fmt_keys or {
            "level": "levelname",
            "message": "message",
            "timestamp": "timestamp",
            "logger": "name",
            "module": "module",
            "function": "funcName",
            "line": "lineno",
            "thread_name": "threadName"
        }
    
    @override
    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record as a JSON string.
        """
        # Create a dictionary for the log record
        log_data = {}
        
        # Add standard record attributes based on fmt_keys mapping
        for output_key, record_attr in self.fmt_keys.items():
            if record_attr == "timestamp":
                # Special handling for timestamp to ensure ISO format
                log_data[output_key] = datetime.datetime.fromtimestamp(
                    record.created
                ).strftime("%Y-%m-%dT%H:%M:%S%z")
            elif hasattr(record, record_attr):
                value = getattr(record, record_attr)
                # Handle callable attributes (like getMessage)
                if callable(value):
                    value = value()
                log_data[output_key] = value
        
        # Add exception info if present
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        # Get the standard LogRecord attribute names from a new empty LogRecord
        standard_attrs = set(logging.LogRecord("", 0, "", 0, "", (), None).__dict__.keys())
        
        # Collect extra attributes in a separate dictionary
        extras = {}
        for key, value in record.__dict__.items():
            if key not in standard_attrs and key not in self.fmt_keys.values():
                extras[key] = value
        
        # Only add the extras field if there are any extra attributes
        if extras:
            log_data["extras"] = extras
        
        # Convert to JSON and return
        return json.dumps(log_data) 