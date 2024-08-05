#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Let's execute multiple coroutines at the same time with async"""
    arr = []
    for _ in range(n):
        data = await wait_random(n, max_delay)

        arr.append(data)
    return arr
