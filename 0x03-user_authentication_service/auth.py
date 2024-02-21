#!/usr/bin/env python3
"""
a _hash_password method that takes in a password
string arguments and returns bytes
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

from typing import Union


def _hash_password(password: str) -> bytes:
    """
    Hash pasword

    Args:
        password (str): description

    Returns:
        bytes: description
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> Union[None, User]:
        """
        Registers new user
        Args:
            email: user email
            password: user password
        Returns:
            User: the user object
        """
        try:
            # Finding the user with a given email
            self._db.find_user_by(email=email)
        except NoResultFound:
            # add user to the database
            return self._db.add_user(email, _hash_password(password))

        else:
            # If the user already exists
            raise ValueError('User {} already exists'.format(email))
