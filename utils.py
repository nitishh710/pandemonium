import time
import logging
from functools import wraps
from typing import Callable, Any

logging.basicConfig(level=logging.INFO)

def telemetry_tracker(func: Callable) -> Callable:
    """Decorator to measure async execution time and simulate rate-limiting."""
    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time
        
        if execution_time > 0.05:
            logging.warning(f"Performance lag in {func.__name__}: {execution_time:.4f}s")
            
        return result
    return wrapper