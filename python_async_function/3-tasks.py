#!/usr/bin/env python3
"""
A module containing a regular function that creates an asyncio.Task
for the wait_random coroutine.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task
    wrapping wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
