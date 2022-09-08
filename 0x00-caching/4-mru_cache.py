#!/usr/bin/env python3
"""creates LIFO class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """LIFO Class"""

    def __init__(self):
        """init method calls super"""
        super().__init__()
        self.mru = None

    def put(self, key, item):
        """Add an item to cache in last position"""
        if key is None or item is None:
            return None
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            print("DISCARD: " + key)
            self.mru = key
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.mru]
            print("DISCARD: " + self.mru)
        self.cache_data[key] = item
        self.mru = key

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        if key in self.cache_data:
            print("I AM HERE")
            self.mru = key
            return self.cache_data[key]
