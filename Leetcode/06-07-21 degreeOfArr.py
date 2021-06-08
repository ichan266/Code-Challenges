# Leetcode # 697
# % Easy (not for me...)
# https://leetcode.com/problems/degree-of-an-array/

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

def findShortestSubArray(num):

    from collections import defaultdict

    numsDict = defaultdict(list)

    for i, num in enumerate(nums):
        numsDict[num].append(i)

    if len(nums) == len(numsDict):
        return 1

    diff = 0
    diffList = []
    degree = max([len(list) for list in numsDict.values()])

    for key, value in numsDict.items():
        if len(value) == degree:
            diff = max(degree, (max(value) - min(value) + 1))
            diffList.append(diff)

    return min(diffList)
