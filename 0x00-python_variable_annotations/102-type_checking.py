#!/usr/bin/env python3
"""Tesing annotation with mypy"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """Function Testing with Anotation Type"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)  # Convert the list back to a tuple


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
