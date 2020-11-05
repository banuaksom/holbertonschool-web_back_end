#!/usr/bin/env python3
""" Regex Task 0 """
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)

    def filter_datum(fields: List[str], redaction: str, message: str,
                     separator: str) -> str:
        """returns the log message obfuscated """
        for f in fields:
            message = re.sub(f'(?<={f}=)[^{separator}]*', redaction, message)
        return message
