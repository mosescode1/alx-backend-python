#!/usr/bin/python3
"""Mixed comples types Annotations"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ype-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns
    their sum as a float."""
    square: float = v * v
    return tuple([k, square])
