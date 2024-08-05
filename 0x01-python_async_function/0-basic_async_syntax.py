#!/usr/bin/python3
import asyncio
from random import uniform
"""The basic of Async"""


async def wait_random(max_delay=10):
    """A couratine"""
    random = uniform(0, max_delay)
    await asyncio.sleep(random)
    return random
