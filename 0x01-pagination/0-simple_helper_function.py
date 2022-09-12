#!/usr/bin/env python3
""" simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """index range of pages top return"""
    return (((page - 1) * page_size), ((page - 1) * page_size) + page_size)
