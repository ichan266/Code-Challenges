# Leetcode # 167
# Two Sum II
# Easy
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def twoSumII_1(numbers, target):

    low, high = 0, len(numbers) - 1

    while low < high:
        total = numbers[low] + numbers[high]
        if total == target:
            return([low + 1, high + 1])
        elif total < target:
            low += 1
        else:
            high -= 1


def twoSumII_2(numbers, target):

    numDict = {}

    for i in range(len(numbers)):
        goal = target - numbers[i]
        if goal in numDict:
            return([numDict[goal] + i, i + 1])
        else:
            numDict[numbers[i]] = i
