#!/usr/bin/env python3
"""
a _hash_password method that takes in a password
string arguments and returns bytes
"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash pasword

    Args:
        password (str): description

    Returns:
        bytes: description
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
