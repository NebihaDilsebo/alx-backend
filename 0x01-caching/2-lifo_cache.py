#!/usr/bin/python3
BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the keys in the order they were added (LIFO)
                keys_in_order = list(self.cache_data.keys())
                # Get the last key added
                last_key = keys_in_order[-1]
                print(f"DISCARD: {last_key}")
                # Remove the last key from the cache
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
