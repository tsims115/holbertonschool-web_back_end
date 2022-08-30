#!/usr/bin/env python3
"""waits randomly"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Awaits randomly"""
    num = uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
