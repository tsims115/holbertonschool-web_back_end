#!/usr/bin/env python3
"""creates LIFO class that inherits from BaseCaching"""

BaseCaching = __import__('baseCaching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Class"""
    def put(self, key, item):
        """Add an item to cache in last position"""
        if key is None or item is None:
            return None
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            print("Discard: ")
            i = 1
            for k, v in self.cache_data.items():
                if i == len(self.cache_data):
                    tmp_key = k
                i += 1
            del self.cache_data[tmp_key]
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
