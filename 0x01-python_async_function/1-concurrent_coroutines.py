#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Let's execute multiple coroutines at the same time with async"""
    arr = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        arr.append(task)
    return [r for r in asyncio.as_completed(arr)]
