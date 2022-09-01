#!/usr/bin/env python3
"""measures runtime"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures runtime"""
    num = time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    return time() - num
