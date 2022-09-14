#!/usr/bin/env python3
"""filter datum obfuscated"""
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
        record.msg = m
        return logging.Formatter(self.FORMAT).format(record)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ get db connection """
    c = mysql.connector.connect(host=os.getenv('PERSONAL_DATA_DB_HOST'),
                                database=os.getenv('PERSONAL_DATA_DB_NAME'),
                                user=os.getenv('PERSONAL_DATA_DB_USERNAME'),
                                password=os.getenv('PERSONAL_DATA_DB_PASSWORD'))
    return c


def get_logger() -> logging.Logger:
    """returns a Logger object"""
    logger = logging.getLogger('user_data')
    stream = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(stream)
    logging.propagate = False
    return logger


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Filters and rerturns obfuscated data"""
    s = separator
    for f in fields:
        message = re.sub(f"{f}=(.*?){s}", f"{f}={redaction}{s}", message)
    return message
