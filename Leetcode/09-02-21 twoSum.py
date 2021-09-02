# Leetcode # 1
# Easy
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum1(nums, target):

    for i in range(len(nums)-1):
        for j in range(1+i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum2(nums, target):

    numsDict = {}

    for i in range(len(nums)):
        goal = target - nums[i]
        if goal in numsDict:
            return [i, numsDict[goal]]
        numsDict[nums[i]] = i
