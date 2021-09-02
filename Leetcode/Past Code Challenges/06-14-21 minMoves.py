# Leetcode # 453
# Easy
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
# In one move, you can increment n - 1 elements of the array by 1.

def minMoves1(nums):
    # increment n - 1 elements equals to decrement 1 element each time
    # if we normalize the elements so that the smaller becomes zero, just sum whatever is left
    minNum = min(nums)
    return sum(num - minNum for num in nums)


# But if we factor out the min(nums) that equals to
def minMoves2(nums):
    return sum(nums) - (min(nums) * len(nums))


#! This one doesn't work! It didn't pass [1, 1, 1000]
def minMovesErr(nums):
    maxNum = max(nums)

    return sum([maxNum - num for num in nums])
