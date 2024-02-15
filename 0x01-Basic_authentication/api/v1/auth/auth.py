#!/usr/bin/env python3
"""
Auth class to manage the API authentication.
"""

from flask import request
from typing import (
    List,
    TypeVar
)


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        this checks whether a given path requires Auth or not
        Args:
            - path (str): URL path to be checked
            - excluded_paths (List of str): List of paths
                that do not require authentication
        Return:
            - True if the path requires authentication, else False
        """
        if path is None:
            return True
        elif excluded_paths in None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
                return True
            
    def authorization_header(self, request=None) -> str:
        """
        Generate the authorization header for the current user.
        This method should be implemented according to your
        authentication logic.
        Returns:
            The authorization header as a string.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user method
        Args:
            self
        Returns:
            None
        """
        return None
