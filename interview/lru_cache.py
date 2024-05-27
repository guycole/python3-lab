#
# Title: lru_cache.py
# Description: 
# 
#
from collections import deque

from typing import Dict


class Solution:
    cache = None
    database = None

    def __init__(self, limit: int):
        self.cache = deque(maxlen=limit)
        self.database = {}

    def get(self, key):
        try:
            ndx = self.cache.index(key)
        except ValueError:
            return -1
        
        self.cache.remove(key)
        self.cache.appendleft(key)
        
        print(f"get: {self.cache}")
        return self.database[key]

    def put(self, key, value):
        limit = self.cache.maxlen
        if len(self.cache) == limit:
            evict = self.cache.pop() # remove the oldest element
            del self.database[evict]

        self.cache.appendleft(key)
        self.database[key] = value

        print(f"put: {self.cache}")

    def execute(self, file_name: str) -> None:
        print("execute")

        return

if __name__ == '__main__':
    print("main")

    solution = Solution(4)
    solution.put(1, 100)
    solution.put(2, 200)
    solution.get(1)
    solution.put(3, 300)
    solution.get(2)
    solution.put(4, 400)
    solution.get(1)
    solution.get(3)
    solution.get(4)
    solution.put(3, 3000)
    solution.get(10000)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
