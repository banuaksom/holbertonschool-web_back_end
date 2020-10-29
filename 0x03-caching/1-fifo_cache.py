#!/usr/bin/python3
''' FIFO caching '''
BaseCaching = __import__('base_caching').BaseCaching
from collections import deque

class FIFOCache(BaseCaching):
    ''' FIFOcashe class '''
    def __init__(self):
        ''' init '''
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        ''' assigns item to the key '''
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                removed = self.queue.popleft()
                del self.cache_data[removed]
                print("DISCARD: " + str(removed))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value of the key '''
        return self.cache_data.get(key)
