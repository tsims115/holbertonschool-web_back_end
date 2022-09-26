#!/usr/bin/env python3
"""auth module
"""
from bcrypt import hashpw, gensalt


def _hash_password(self, password: str) -> bytes:
        """Hashes and salts the password"""
        salt = gensalt()
        hashed = hashpw(password.encode('utf8'), salt)
        return hashed
