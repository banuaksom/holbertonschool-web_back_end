#!/usr/bin/python3
''' MRU caching '''
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' MRUcashe class '''
    def __init__(self):
        ''' init constructor'''
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        ''' assigns item to the key '''
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                removed = self.queue.pop()
                del self.cache_data[removed]
                print("DISCARD: " + str(removed))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value of the key '''
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
