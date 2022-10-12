#!/usr/bin/env python3
""" Cache class """
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps

def replay(fn: Callable):
    """display history of calls for a particular function"""
    redd = redis.Redis()
    name = cache.store.__qualname__
    inputs = redd.lrange("{}:inputs".format(name), 0, -1)
    outputs = redd._redis.lrange("{}:outputs".format(name), 0, -1)
    print(f"{name} was called {len(inputs)} times:")
    for i, o in zip(inputs, outputs):
        print(f'{name}(*({name},)) -> {o}')

def count_calls(method: Callable) -> Callable:
    """Counts the number of method calls"""
    k = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(k)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs"""
    k = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(k + ":inputs", str(args))
        op = method(self, *args, **kwargs)
        self._redis.rpush(k + ":outputs", op)
        return op
    return wrapper


class Cache:
    """Cache Class"""

    def __init__(self):
        """initializes the Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
