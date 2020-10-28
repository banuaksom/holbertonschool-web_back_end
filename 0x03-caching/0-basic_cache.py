#!/usr/bin/python3
''' Basic dictionary '''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key)