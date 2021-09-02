# Leetcode # 1370
# https://leetcode.com/problems/increasing-decreasing-string/

# Given a string s. You should re-order the string using the following algorithm:

# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

# Return the result string after sorting s with this algorithm.

import collections


def sortString(s: str) -> str:

    result = ''
    available = collections.Counter(s)
    unique = sorted(available.keys())

    while len(result) < len(s):
        for char in unique:
            if available[char]:
                available[char] -= 1
                result += char
        unique = unique[::-1]

    return result
