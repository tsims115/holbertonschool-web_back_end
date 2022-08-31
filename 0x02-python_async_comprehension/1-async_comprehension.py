#!/usr/bin/env python3
""" collects to random numbers using the asyunc_generator """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """ collects to random numbers using the asyunc_generator """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
