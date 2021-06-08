# Leetcode #229
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)/3
        
        countDict = {}
        
        for num in nums:
            countDict[num] = countDict.get(num, 0) + 1
        
        result = [item[0] for item in countDict.items() if item[1] > n]
                
        return result

instance = Solution()
print(instance.majorityElement([1,2]))