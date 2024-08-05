#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Let's execute multiple coroutines at the same time with async"""
    arr = []
    for _ in range(n):
        data = await task_wait_random(max_delay)

        arr.append(data)
    return arr
