# Leetcode # 1470
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

from typing import List

# This is a faster solution (comparing to the second one)
class Solution:
    def shuffle1(self, nums: List[int], n: int) -> List[int]:
        
        result = []
        
        for index in range(n):
            result.extend([nums[index], nums[index+n]])
        
        return result

    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        
        ls1 = nums[:n]
        ls2 = nums[n:]
        
        result = []
        
        for num1, num2, in zip(ls1, ls2):
            result.extend([num1, num2])
        
        return result