#!/usr/bin/env python3
"""filter datum obfuscated"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.f = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters log and formats it"""
        m = filter_datum(self.f, self.REDACTION, record.msg, self.SEPARATOR)
        record.msg = '; '.join(m.split(';'))
        formatter = logging.Formatter(self.FORMAT)
        return formatter.format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                  separator: str) -> str:
    """Filters and rerturns obfuscated data"""
    s = separator
    for f in fields:
        message = re.sub(f"{f}=(.*?){s}", f"{f}={redaction}{s}", message)
    return message
