# Leetcode # 27
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        read, write = 0, 0

        while read < len(nums):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
            read += 1

        return write
