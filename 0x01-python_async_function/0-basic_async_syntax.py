#!/usr/bin/python3
"""The basic of Async"""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """A couratine"""
    random = uniform(0, max_delay)
    await asyncio.sleep(random)
    return random
