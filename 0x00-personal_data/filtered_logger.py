#!/usr/bin/env python3
"""
Regex-ing function that returs a log message obfuscated
"""


from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        seperator: str) -> str:
    """
    function that returns the log message obfuscated

    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field
        will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character
        is separating all fields in the log line

    Returns:
        returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{seperator}',
                         f'{field}={redaction}{seperator}', message)
    return message
