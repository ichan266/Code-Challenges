# Leetcode # 146
# LRU Cache
# Medium
# Design a data structure that follows the constraints of a Least Recently Used(LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# @ Leetcode Solution using OrderedDict from Python's collections module
from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# % Using OrderedDict in collections, the object itself is the ordered dictionary when we instantiate it. Because we need to keep track of order for whenever we see the key, every time we see a valid key, the very first thing we need to do is to move it to the end of the ordered dictionary by using the move_to_end(key) method (here, we pass the key in as an argument in order to move the key:value pair to the end). And when the ordered dictionary reached its capacity, we remove the first item in the dictionary by using popitem(last=False). Note that if we don't pass "last=False" as an argument, it will pop the last item on the right (i.e. end of the dictionary)
