# Understanding the Transaction Management Code

Let's break down this transaction management code step by step:

## 1. Imports and Setup

```python
import time
import logging
import psycopg2
from contextlib import contextmanager
from typing import Optional, Callable, Any
from app.database.db_common import get_connection
from app.config.settings import settings

# Configure logging
logger = logging.getLogger(__name__)
```

This section:
- Imports necessary libraries (time for measuring duration, logging for feedback)
- Sets up a logger for this module

## 2. Custom Exception Classes

```python
class TransactionError(Exception):
    """Exception raised for transaction-related errors."""
    pass

class TransactionTimeout(TransactionError):
    """Exception raised when a transaction times out."""
    pass
```

These are custom exception classes:
- `TransactionError`: A general error for any transaction problems
- `TransactionTimeout`: A specific error for when transactions take too long (inherits from TransactionError)

## 3. The Main Transaction Context Manager

```python
@contextmanager
def transaction(
    use_neon: Optional[bool] = None,
    timeout: Optional[float] = None,
    feedback: bool = True,
    auto_rollback: bool = True
):
```

This is a context manager (used with `with` statements) that:
- Takes parameters to control behavior:
  - `use_neon`: Whether to use Neon database (overrides settings)
  - `timeout`: Maximum seconds to allow for the transaction
  - `feedback`: Whether to log what's happening
  - `auto_rollback`: Whether to automatically rollback on errors

## 4. Transaction Setup

```python
conn = None
start_time = time.time()
db_type = "Neon" if (use_neon if use_neon is not None else settings.use_neon) else "local"

try:
    # Get database connection
    if feedback:
        logger.info(f"Starting transaction with {db_type} database")
    
    conn = get_connection(use_neon=use_neon)
```

This part:
- Initializes variables (connection and start time)
- Determines which database to use
- Logs the start of the transaction (if feedback is enabled)
- Gets a database connection

## 5. Setting Timeout

```python
# Set timeout if specified
if timeout is not None and timeout > 0:
    # Set statement timeout in milliseconds
    with conn.cursor() as cur:
        cur.execute(f"SET statement_timeout = {int(timeout * 1000)}")
```

This sets a PostgreSQL statement timeout if one was specified:
- Converts seconds to milliseconds
- Tells PostgreSQL to abort any statement that takes longer than this time

## 6. Yielding the Connection

```python
# Yield connection to the caller
yield conn
```

This is where the context manager pauses and gives control to the code inside the `with` block.
- The connection is passed to your code to use
- When your code finishes, execution continues after this line

## 7. Committing the Transaction

```python
# Check timeout before committing
if timeout is not None and (time.time() - start_time) > timeout:
    raise TransactionTimeout(f"Transaction timed out after {timeout} seconds")

# Commit the transaction
conn.commit()

if feedback:
    duration = time.time() - start_time
    logger.info(f"Transaction committed successfully ({duration:.2f}s)")
```

After your code finishes:
- It checks if we've exceeded the timeout
- If not, it commits the transaction (saves changes to the database)
- Logs the successful commit with duration

## 8. Handling Connection Errors

```python
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
```

This handles database connection errors:
- Checks if it's a timeout error
- Logs the error
- Rolls back the transaction if auto_rollback is enabled
- Raises a custom exception

## 9. Handling Other Exceptions

```python
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
```

This handles any other exceptions:
- Logs the error with duration
- Rolls back the transaction if auto_rollback is enabled
- Re-raises the original exception

## 10. Cleanup

```python
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
```

This cleanup always runs:
- Closes the database connection
- Logs any errors that occur during closing

## 11. Helper Function

```python
def execute_with_transaction(
    func: Callable,
    *args,
    use_neon: Optional[bool] = None,
    timeout: Optional[float] = None,
    feedback: bool = True,
    auto_rollback: bool = True,
    **kwargs
) -> Any:
```

This is a helper function that:
- Takes a function and its arguments
- Takes the same transaction parameters
- Executes the function within a transaction

```python
with transaction(
    use_neon=use_neon,
    timeout=timeout,
    feedback=feedback,
    auto_rollback=auto_rollback
) as conn:
    return func(conn, *args, **kwargs)
```

It:
- Creates a transaction using the context manager
- Calls your function with the connection and other arguments
- Returns whatever your function returns

This helper makes it easier to use transactions without writing the `with` statement every time.

## 12 Usage Example

```python
from app.database.transaction import transaction, execute_with_transaction, TransactionError, TransactionTimeout

def insert_chunk(conn, text, vector, metadata):
    """Insert a chunk into the database."""
    # ... existing implementation ...
    return chunk_id

def insert_chunk_with_transaction(text, vector, metadata, use_neon=None, timeout=None):
    """Insert a chunk with transaction management."""
    try:
        with transaction(use_neon=use_neon, timeout=timeout) as conn:
            chunk_id = insert_chunk(conn, text, vector, metadata)
            return chunk_id
    except TransactionTimeout:
        print("Insert operation timed out")
        return None
    except TransactionError as e:
        print(f"Transaction error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Alternative using the execute_with_transaction helper
def insert_chunk_with_helper(text, vector, metadata, use_neon=None, timeout=None):
    """Insert a chunk using the transaction helper."""
    return execute_with_transaction(
        insert_chunk,
        text, vector, metadata,
        use_neon=use_neon,
        timeout=timeout
    )
```
