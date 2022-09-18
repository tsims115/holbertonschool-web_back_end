#!/usr/bin/env python3
""" holds auth class """
from flask import request
from typing import TypeVar, List

class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Implement later"""
        return False

    def authorization_header(self, request=None) -> str:
        """Implement later"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Implement later"""
        return None
