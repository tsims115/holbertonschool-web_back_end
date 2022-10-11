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

    def get(self, key: str, fn: Callable = None):
        """gets data from with given key"""
        if fn is not None:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self):
        """get string method"""
        return self._redis.get(key).decode("utf-8")

    def get_int(self):
        """get int method"""
        return int(self._redis.get(key))
