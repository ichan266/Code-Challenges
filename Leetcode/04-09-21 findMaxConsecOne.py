# Leetcode #485
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# First study session with Monisha. This is a question given by Monisha.

def findMaxConsecutiveOnes(nums: list[int]) -> int:

    countSet = set()
    count = 0

    for num in nums:
        if num == 1:
            count += 1
        elif num != 1:
            countSet.add(count)
            count = 0

    countSet.add(count)

    return max(countSet)


def findMaxConsecutiveOnes1(nums: list[int]) -> int:

    # countSet = set()
    count, maxCount = 0, 0

    for num in nums:
        if num == 1:
            count += 1
        elif num != 1:
            maxCount = max(count, maxCount)
            count = 0

    maxCount = max(count, maxCount)

    return maxCount


# can also use string manupulation


print(findMaxConsecutiveOnes([1, 0, 1, 0, 1, 1]))
