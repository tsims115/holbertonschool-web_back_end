#!/usr/bin/env python3
"""auth module
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
        """Hashes and salts the password"""
        return hashpw(password.encode('utf8'), gensalt())
