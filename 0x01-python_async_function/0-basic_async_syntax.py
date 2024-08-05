#!/usr/bin/python3
"""The basic of Async function"""
import asyncio
from random import uniform

if __name__ == "__main__":

    async def wait_random(max_delay=10) -> float:
        """A couratine for async function"""
        random = uniform(0, max_delay)
        await asyncio.sleep(random)
        return random
