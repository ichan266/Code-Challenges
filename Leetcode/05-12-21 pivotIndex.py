# Leetcode # 724
# https://leetcode.com/problems/find-pivot-index/

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(nums: list[int]) -> int:

    total = sum(nums)

    leftSum = 0

    for index, num in enumerate(nums):
        rightSum = total - leftSum - num
        # checking if left and right sum are equal. If they are, that means if it crosses pivot.
        if leftSum == rightSum:
            return index
        leftSum += num

    return -1
