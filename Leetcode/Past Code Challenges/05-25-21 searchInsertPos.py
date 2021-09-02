# Leetcode #35
# https://leetcode.com/problems/search-insert-position/

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums, target):

    if target < nums[0]:
        return 0
#         if target > nums[-1]:
#             return len(nums)

    left = 0
    right = len(nums)-1

    while True:
        mid = (left + right) // 2
        if left >= right:
            if nums[mid] < target:
                return mid + 1
            else:
                return mid
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
