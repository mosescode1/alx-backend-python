#!/usr/bin/env python3
""""""
from time import perf_counter
import asyncio
async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = perf_counter()
    arr = []
    for _ in range(4):
        arr.append(async_comprehension())

    await asyncio.gather(*arr)

    times = perf_counter() - start
    return times
