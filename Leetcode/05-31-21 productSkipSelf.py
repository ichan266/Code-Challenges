# Leetcode # 238
# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):

    # construct forward list
    result = [1]
    for i in range(len(nums)-1):
        result.append(result[-1]*nums[i])

    product = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] = product * result[i]
        product *= nums[i]

    return result
