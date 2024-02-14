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
        pass
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user method
        Args:
            self
        Returns:
            None
        """
        return None