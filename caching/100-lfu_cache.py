#!/usr/bin/python3
''' LFU Caching: Create a class LFUCache that inherits from BaseCaching
                 and is a caching system '''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' An LFU cache.
        Inherits all behaviors from BaseCaching except, upon any attempt to add
        an entry to the cache when it is at max capacity (as specified by
        BaseCaching.MAX_ITEMS), it discards the least frequently used entry to
        accommodate for the new one.
        Attributes:
          __init__ - method that initializes class instance
          put - method that adds a key/value pair to cache
          get - method that retrieves a key/value pair from cache '''

    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """dictionary
        """
        if key or item is not None:
            valuecache = self.get(key)
            # Make a new
            if not key or not item:
                return
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = self.leastrecent
                    lendel = len(keydel) - 1
                    del self.cache_data[keydel[lendel]]
                    print("DISCARD: {}".format(self.leastrecent.pop()))
            else:
                del self.cache_data[key]

            if key in self.leastrecent:
                idxtodel = self.search_first(self.leastrecent, key)
                self.leastrecent.pop(idxtodel)
                self.leastrecent.insert(0, key)
            else:
                self.leastrecent.insert(0, key)

            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked
        """
        valuecache = self.cache_data.get(key)
        if not key or key not in self.cache_data:
            return None
        if valuecache:
            idxtodel = self.search_first(self.leastrecent, key)
            self.leastrecent.pop(idxtodel)
            self.leastrecent.insert(0, key)

        return valuecache

    def discard(self):
        """
        discard item and print
        """
        m_time = min(self.__counter.values())
        keys = [k for k, v in self.__counter.items() if v == m_time]
        low = 0
        while self.__keys[low] not in keys:
            low += 1
        discard = self.__keys.pop(low)
        del self.cache_data[discard]
        del self.__counter[discard]
        print('DISCARD: {}'.format(discard))
