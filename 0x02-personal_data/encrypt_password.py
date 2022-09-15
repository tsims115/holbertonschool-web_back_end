#!/usr/bin/env python3
"""
encryption
"""
import bcrypt
 

def hash_password(p: str) -> bytes:
    """hashes password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(p.encode('utf8'), salt)
    return hashed
