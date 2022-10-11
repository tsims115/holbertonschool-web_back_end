#!/usr/bin/env python3
""" Cache class """
import redis
from uuid import uuid4
from typing import Union

class Cache:
    """Cache Class"""

    def __init__(self):
        """initializes the Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates key"""
        uid = uuid4()
        r.set(uid, data)
        return uid
