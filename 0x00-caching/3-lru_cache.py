#!/usr/bin/env python3
"""creates LRU class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Class"""

    def __init__(self):
        """init method calls super"""
        super().__init__()
        self.last = None
        self.cnt = 0
        self.lru = {}

    def put(self, key, item):
        """Add an item to cache in last position"""
        if key is None or item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache_data.pop(old_key)
            self.lru.pop(old_key)
            print("DISCARD: " + old_key)
        self.cache_data[key] = item
        self.lru[key] = self.cnt
        self.cnt += 1
        

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
