#!/usr/bin/python3
""" BasicCache class that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A caching system that doesn't have a limit """

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)
