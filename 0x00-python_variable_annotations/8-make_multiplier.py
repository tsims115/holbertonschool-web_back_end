#!/usr/bin/env python3
"""multiplies by multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies by multiplier"""
    def multi(num: float) -> float:
        """returns the multiplied numbered"""
        return num * multiplier
    return multi
