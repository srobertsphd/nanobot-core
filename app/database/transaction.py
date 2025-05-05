"""
Transaction Management Module

*This module is currently not used in production code.*

This module provides utilities for managing database transactions with
error handling, logging, timeouts, and automatic rollback.
"""

import time
import logging
import psycopg2
from contextlib import contextmanager
from typing import Optional, Callable, Any
from app.database.common import get_connection
from app.config.settings import settings

# Configure logging
logger = logging.getLogger(__name__)

class TransactionError(Exception):
    """Exception raised for transaction-related errors."""
    pass

class TransactionTimeout(TransactionError):
    """Exception raised when a transaction times out."""
    pass

@contextmanager
def transaction(
    use_neon: Optional[bool] = None,
    timeout: Optional[float] = None,
    feedback: bool = True,
    auto_rollback: bool = True
):
    """
    Context manager for database transactions with advanced features.
    
    Args:
        use_neon: Override settings.use_neon flag. If None, uses settings value.
        timeout: Maximum time in seconds to wait for transaction to complete.
                 None means no timeout.
        feedback: Whether to log transaction events.
        auto_rollback: Whether to automatically rollback on exception.
    
    Yields:
        psycopg2.connection: Database connection
    
    Raises:
        TransactionTimeout: If the transaction exceeds the timeout.
        TransactionError: For other transaction-related errors.
        Exception: Any exception raised during the transaction.
    """
    conn = None
    start_time = time.time()
    db_type = "Neon" if (use_neon if use_neon is not None else settings.use_neon) else "local"
    
    try:
        # Get database connection
        if feedback:
            logger.info(f"Starting transaction with {db_type} database")
        
        conn = get_connection(use_neon=use_neon)
        
        # Set timeout if specified
        if timeout is not None and timeout > 0:
            # Set statement timeout in milliseconds
            with conn.cursor() as cur:
                cur.execute(f"SET statement_timeout = {int(timeout * 1000)}")
        
        # Yield connection to the caller
        yield conn
        
        # Check timeout before committing
        if timeout is not None and (time.time() - start_time) > timeout:
            raise TransactionTimeout(f"Transaction timed out after {timeout} seconds")
        
        # Commit the transaction
        conn.commit()
        
        if feedback:
            duration = time.time() - start_time
            logger.info(f"Transaction committed successfully ({duration:.2f}s)")
    
    except psycopg2.OperationalError as e:
        if "statement timeout" in str(e).lower():
            if feedback:
                logger.error(f"Transaction timed out after {timeout} seconds")
            raise TransactionTimeout(f"Database operation timed out after {timeout} seconds") from e
        
        if feedback:
            logger.error(f"Database connection error: {e}")
        
        if conn and auto_rollback:
            try:
                conn.rollback()
                if feedback:
                    logger.info("Transaction rolled back due to connection error")
            except Exception as rollback_error:
                if feedback:
                    logger.error(f"Failed to rollback transaction: {rollback_error}")
        
        raise TransactionError(f"Database connection error: {e}") from e
    
    except Exception as e:
        duration = time.time() - start_time
        
        if feedback:
            logger.error(f"Transaction failed after {duration:.2f}s: {e}")
        
        if conn and auto_rollback:
            try:
                conn.rollback()
                if feedback:
                    logger.info("Transaction rolled back due to error")
            except Exception as rollback_error:
                if feedback:
                    logger.error(f"Failed to rollback transaction: {rollback_error}")
        
        # Re-raise the original exception
        raise
    
    finally:
        # Close connection in finally block to ensure it happens
        if conn:
            try:
                conn.close()
                if feedback:
                    logger.debug("Database connection closed")
            except Exception as close_error:
                if feedback:
                    logger.error(f"Error closing database connection: {close_error}")

def execute_with_transaction(
    func: Callable,
    *args,
    use_neon: Optional[bool] = None,
    timeout: Optional[float] = None,
    feedback: bool = True,
    auto_rollback: bool = True,
    **kwargs
) -> Any:
    """
    Execute a function within a transaction context.
    
    Args:
        func: Function to execute. First argument must accept a database connection.
        *args: Arguments to pass to the function.
        use_neon: Override settings.use_neon flag.
        timeout: Maximum time in seconds for the transaction.
        feedback: Whether to log transaction events.
        auto_rollback: Whether to automatically rollback on exception.
        **kwargs: Keyword arguments to pass to the function.
    
    Returns:
        Any: Result of the function.
    
    Raises:
        TransactionTimeout: If the transaction exceeds the timeout.
        TransactionError: For other transaction-related errors.
        Exception: Any exception raised by the function.
    """
    with transaction(
        use_neon=use_neon,
        timeout=timeout,
        feedback=feedback,
        auto_rollback=auto_rollback
    ) as conn:
        return func(conn, *args, **kwargs) 