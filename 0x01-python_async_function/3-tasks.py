#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import Any, Dict, Optional, Union
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Any:
    """Let's execute multiple coroutines at the same time with async"""
    return asyncio.Task(wait_random(max_delay))
