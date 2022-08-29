#!/usr/bin/env python3
"""string and int/float"""

from typing import List, Union, Tuple

itypes = Union[int, float]
ttypes = Union[str, float]


def to_kv(k: str, v: itypes) -> Tuple[str, float]:
    """string and int/float Tuple"""
    return (k, v * v)
