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

    def __init__(self, fields: List[int]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters log and formats it"""
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        record.msg = '; '.join(record.msg.split(';'))
        formatter = logging.Formatter(self.FORMAT)
        return formatter.format(record)


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Filters and rerturns obfuscated data"""
    for f in fields:
        tmp=re.split(separator,message[re.search(f,message).span()[1]+1:])
        message = re.sub(tmp[0], redaction, message)
    return message
