#!/usr/bin/env python3
"""creates LIFO class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Class"""

    def __init__(self):
        """init method calls super"""
        super().__init__()
        self.last = None

    def put(self, key, item):
        """Add an item to cache in last position"""
        if key is None or item is None:
            return None
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            print("DISCARD: " + key)
            self.last = key
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last]
            print("DISCARD: " + self.last)
        self.cache_data[key] = item
        self.last = key

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
