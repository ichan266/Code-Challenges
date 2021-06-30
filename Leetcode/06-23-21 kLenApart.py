# Leetcode # 1437
# Easy
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

# Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

def kLengthApart(nums, k):

    currentRun = k  # Have to use k instead of 0 to pass through the first "1" in nums

    for num in nums:
        if num == 1:
            if currentRun < k:
                return False
            currentRun = 0
        else:
            currentRun += 1

    return True
