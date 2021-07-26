# Leetcode #49 - Group Anagrams
# Medium
# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# @ This one works! It is O(n) by using the sorted word as the key and throw the same anagrams into the a bucket (value is a list of the anagrams)
def groupAnagrams(strs):

    result = {}

    for word in strs:
        key = "".join(sorted(word))
        result[key] = result.get(key, [])
        result[key].append(word)

    return result.values()


# * This one will work too but not efficient because of O(n2). It ran into Exceed Time Limit
def groupAnagrams2(strs):

    if len(strs) == 1:
        return [strs]

    finalResult = []
    seenIdx = set()

    for idx1, word1 in enumerate(strs):
        if idx1 in seenIdx:
            continue
        seenIdx.add(idx1)
        currentList = [word1]
        for idx2, word2 in enumerate(strs[idx1+1:]):
            if len(word1) != len(word2):
                continue
            elif sorted(word1) == sorted(word2):
                currentList.append(word2)
                seenIdx.add(idx1+idx2+1)
        finalResult.append(currentList)
        del currentList

    return finalResult
