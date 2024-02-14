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
            path of the auth, thie is the url to be checked
            exluded_path, this is a list of paths that dont require
            Authentication
        Return:
            False if the path is included in excluded_paths
        """
        if path is None:
            return True
        elif excluded_paths in None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        
        
        return path not in excluded_paths

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
