# Leetcode #387
# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.


def firstUniqChar1(s: str) -> int:

    for index, char in enumerate(s):
        if s.count(char) == 1:
            return index

    return -1


def firstUniqChar2(s: str) -> int:

    countDict = {}

    for char in s:
        countDict[char] = countDict.get(char, 0) + 1

    for index, letter in enumerate(s):
        if countDict[letter] == 1:
            return index

    return -1
