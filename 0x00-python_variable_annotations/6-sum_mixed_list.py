#!/usr/bin/env python3
"""Mixed comples types Annotations"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ype-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns
    their sum as a float."""
    return float(sum(mxd_lst))
