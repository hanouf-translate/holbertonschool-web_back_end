#!/usr/bin/env python3
"""
An asynchronous generator coroutine that yields a random number
between 0 and 10 after waiting 1 second, 10 times.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times, asynchronously wait 1 second each time,
    and yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
