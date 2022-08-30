#!/usr/bin/env python3
"""take two ints and calls wait_random"""

from random import uniform
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """calls wait_random n amount of times"""
    delay_list = [wait_random(max_delay) for i in range(n)]
    wait_times = []
    for item in asyncio.as_completed(delay_list):
        wait_times.append(await item)
    return wait_times
