#!/usr/bin/env python3
"""
filtered_logger.py
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated
    """
    for word in fields:
        obfuscated = re.sub(f'{word}=.*?{separator}',
                            f'{word}={redaction}{separator}', message)
    return obfuscated
