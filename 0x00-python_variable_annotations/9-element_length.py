#!/usr/bin/env python3
"""elements lengths returned"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """elements lengths returned"""
    return [(i, len(i)) for i in lst]
