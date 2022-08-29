#!/usr/bin/env python3
"""mixed list"""

from typing import List, Union

types = Union[int, float]


def sum_mixed_list(mxd_lst: List[types]) -> float:
    """mixed list and returns the sum"""
    sum: float
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
