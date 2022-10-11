#!/usr/bin/env python3
""" Cache class """
import redis
from uuid import uuid4
from typing import Union, Callable

class Cache:
    """Cache Class"""

    def __init__(self):
        """initializes the Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates key"""
        uid = str(uuid4())
        self._redis.set(uid, data)
        return uid

    def get(self, key: str, fn: Callable):
        """gets data from with given key"""
        print(self._redis.get(key))
        if fn is not None:
            return fn(self._redis.get(key))
        return self._redis.get(key)