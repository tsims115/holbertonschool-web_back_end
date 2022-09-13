#!/usr/bin/env python3
"""filter datum obfuscated"""
from typing import List
from re import sub, split, search


def filter_datum(fields: List[str], redaction: str, message: str, seperator: str) -> str:
    """Filters and rerturns obfuscated data"""
    for f in fields:
        tmp = split(seperator, message[search(f, message).span()[1] + 1:])
        message = sub(tmp[0], redaction, message)
    return message
