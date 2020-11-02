#!/usr/bin/env python3
""" Regex Task 0 """
from typing import List
import re

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ returns the log message """
    for f in fields:
        message = re.sub(f'(?<={f}=)[^{separator}]*', redaction, message)
    return message
