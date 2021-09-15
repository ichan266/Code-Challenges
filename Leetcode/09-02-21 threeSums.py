# Leetcode # 15
# Three Sums
# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

import collections


def threeSum(nums):

    result = set()
    counts = collections.Counter(nums)
    nums = []

    for key in counts:
        nums.extend([key] * min(counts[key], 3))

    nums.sort()
    for i in range(len(nums)-2):
        target = 0 - nums[i]
        low = 0
        high = len(nums)-1
        while low < high:
            if low == i:
                low += 1
            if high == i:
                high -= 1
            if (low == high):
                break

            total = nums[low] + nums[high]
            if total == target:
                result.add(tuple(sorted((nums[i], nums[high], nums[low]))))
                low += 1
            elif total < target:
                low += 1
            elif total > target:
                high -= 1

    return result
