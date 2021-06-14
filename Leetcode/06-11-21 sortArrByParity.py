# Leetcode # 905
# Easy
# https://leetcode.com/problems/sort-array-by-parity/

# Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums. You may return any answer array that satisfies this condition.

# * Classic way of sorting it: throwing them into 2 buckets with one odd and one even.
# * Time Complexity: O(n)       Space Complexity: O(n)
def sortArrayByParity1(nums):
    odd, even = [], []
    for num in nums:
        even.append(num) if num % 2 == 0 else odd.append(num)

    return even + odd


# * List comprehension (basically same as above but condensed into one single line)
def sortArrayByParity2(nums):

    return [n for n in nums if n % 2 == 0] + [n for n in nums if n % 2 == 1]


# * Sort the list using lambda as the key
# * Time Complexity: O(n log n)       Space Complexity: O(n)
def sortArrayByParity3(nums):
    nums.sort(key=lambda x: x % 2)
    return nums


# * In-place swap 1 (Iris' version)
# * Time Complexity: O(n)       Space Complexity: O(1)
def sortArrayByParity4(nums):
    walkIdx, waitingIdx = 0, 0

    while walkIdx < len(nums):
        if nums[walkIdx] % 2 == 0:
            nums[walkIdx], nums[waitingIdx] = nums[waitingIdx], nums[walkIdx]
            waitingIdx += 1
        walkIdx += 1

    return nums


# * In-place swap 2 (Leetcode's version)
# * Time Complexity: O(n)       Space Complexity: O(1)
def sortArrayByParity5(nums):
    startIdx, endIdx = 0, len(nums)-1

    while startIdx < endIdx:
        if nums[startIdx] % 2 == 1:
            nums[startIdx], nums[endIdx] = nums[endIdx], nums[startIdx]
        if nums[startIdx] % 2 == 0:
            startIdx += 1
        if nums[endIdx] % 2 == 1:
            endIdx -= 1

    return nums
