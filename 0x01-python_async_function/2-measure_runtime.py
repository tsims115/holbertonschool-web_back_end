#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the runtime"""
    time_in_seconds = time()
    asyncio.run(wait_n(n, max_delay))
    time_in_seconds = time() - time_in_seconds
    return time_in_seconds / n
