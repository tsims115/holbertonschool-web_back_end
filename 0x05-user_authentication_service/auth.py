#!/usr/bin/env python3
"""auth module
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashes and salts the password"""
    return hashpw(password.encode('utf8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Inistializes the class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers new user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError('User ' + email + " already exists")
        except NoResultFound:
            password = _hash_password(password)
            return self._db.add_user(email, password)

    def valid_login(self, email: str, password: str) -> bool:
        """checks if the user password is valid"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if checkpw(password.encode('utf-8'), user.hashed_password):
            return True
        return False
