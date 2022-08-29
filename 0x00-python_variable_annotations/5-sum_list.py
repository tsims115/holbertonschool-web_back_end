#!/usr/bin/env python3
"""defines annotations"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """defines annotations"""
    sum: float
    sum = 0
    for i in input_list:
        sum += i
    return sum
