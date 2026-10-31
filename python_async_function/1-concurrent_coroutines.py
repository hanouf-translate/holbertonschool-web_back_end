#!/usr/bin/env python3
"""
An asynchronous routine that spawns wait_random n times
with a specified max_delay and returns the list of all delays in ascending order.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    and return the list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays
