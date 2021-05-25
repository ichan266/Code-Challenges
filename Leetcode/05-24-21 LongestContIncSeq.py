# Leetcode # 674
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

def findLengthOfLCIS(nums) -> int:
    
    count = 0
    subCount = 1
    
    for i in range(len(nums)-1):
        if nums[i+1] > nums[i]:
            subCount += 1
        else:
            count = max(count, subCount)
            subCount = 1

    count = max(count, subCount)
        
    return count
