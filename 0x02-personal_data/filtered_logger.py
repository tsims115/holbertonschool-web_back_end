#!/usr/bin/env python3
"""filter datum obfuscated"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, seperator: str) -> str:
    """Filters and rerturns obfuscated data"""
    for f in fields:
        tmp = re.split(seperator, message[re.search(f, message).span()[1] + 1:])
        message = re.sub(tmp[0], redaction, message)
    return message
