# Leetcode # 3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# @ My solution. Runtime O(n2)
def lengthOfLongestSubstring1(s):

    result = 0

    for i, letterOut in enumerate(s):
        count = 1
        currentSet = {letterOut}
        for letterIn in s[i+1:]:
            if letterOut != letterIn and letterIn not in currentSet:
                count += 1
                currentSet.add(letterIn)
            else:
                break
        if count > result:
            result = count

    return result

# * Ben's solution. Runtime O(n)


def lengthOfLongestSubstring2(s):

    result = 0
    start = 0

    lastInstances = {}

    for i, c in enumerate(s):
        if c in lastInstances:
            start = max(start, lastInstances[c]+1)
        lastInstances[c] = i
        result = max(i-start+1, result)

    return result
