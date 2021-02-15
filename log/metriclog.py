import functools
import time
from log.logger import get_logger


def metric_log(key: str):
    def decorator(func):
        @functools.wraps(func)
        def metric_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            run_time = time.perf_counter() - start_time     # seconds
            logger = get_logger()
            logger.metric(key, int(round(run_time*1000)))
            return value
        return metric_wrapper
    return decorator
