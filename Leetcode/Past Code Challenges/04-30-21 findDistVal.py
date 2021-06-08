# Leetcode # 1385
# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        count = 0

        for num1 in arr1:
            for num2 in arr2:
                if abs(num1-num2) <= d:
                    break
            else:
                count += 1

        return count
