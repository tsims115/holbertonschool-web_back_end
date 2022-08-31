#!/usr/bin/env python3
""" async generator """
from random import uniform
import asyncio

async def async_generator() -> float:
    """ async generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
