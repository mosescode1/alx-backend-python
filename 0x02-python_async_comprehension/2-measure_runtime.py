#!/usr/bin/env python3
""""""
from time import perf_counter
import asyncio
async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    time = perf_counter() - start
    return time
