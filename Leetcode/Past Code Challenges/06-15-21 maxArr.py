# Leetcode # 53
# Easy
# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
def maxSubArray(nums):

    bestSum = nums[0]
    total = 0

    for current in nums:
        total = total + current
        bestSum = max(total, bestSum)
        if total < 0:
            total = 0

    return bestSum
