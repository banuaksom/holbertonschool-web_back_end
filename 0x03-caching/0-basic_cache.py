#!/usr/bin/python3
''' Basic dictionary '''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCashe class '''
    def put(self, key, item):
        ''' assigns item for the key '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' returns the value linked to the key'''
        return self.cache_data.get(key)
