#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function for a mul"""
    def func(mul: float) -> float:
        return mul * multiplier
    return func
