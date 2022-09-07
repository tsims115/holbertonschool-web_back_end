#!/usr/bin/env python3
"""creates FIFO class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO class"""
    def put(self, key, item):
        """Add an item to cache in last position"""
        if key == None or item == None:
            return None
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for k, v in self.cache_data.items():
                del self.cache_data[k]
                print("DISCARD: " + k)
                break

    def get(self, key):
        """Get an item by key"""
        if key == None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
            