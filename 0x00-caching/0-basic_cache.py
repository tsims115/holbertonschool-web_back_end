#!/usr/bin/python3
"""caching system inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching"""
    def put(self, key, item):
        """Add an item to cache"""
        if key == None or item == None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key == None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
