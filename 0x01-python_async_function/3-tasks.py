#!/usr/bin/env python3
""" returns a asyncrio task """
from random import uniform
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ returns a asyncrio task """
    return asyncio.create_task(wait_random(max_delay))
