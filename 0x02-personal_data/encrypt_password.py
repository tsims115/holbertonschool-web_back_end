#!/usr/bin/env python3
"""
encryption
"""
import bcrypt
 

def hash_password(password: str) -> bytes:
    """hashes password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf8'), salt)
    return hashed
