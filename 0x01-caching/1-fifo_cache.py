#!/usr/bin/python3
"""FIFOCache class that inherits from BaseCaching"""

from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A caching system that uses the FIFO algorithm """

    def __init__(self):
        """initializes the FIFO cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache using FIFO strategy """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the first item (the one to be discarded)
                first_item_key = next(iter(self.cache_data))
                # Delete the first item and print DISCARD message
                del self.cache_data[first_item_key]
                print(f"DISCARD: {first_item_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)




