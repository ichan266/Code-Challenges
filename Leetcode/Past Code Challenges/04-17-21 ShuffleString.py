# Leetcode 1528
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string. Return the shuffled string.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        newList = [0] * len(s)
        
        for index in range(len(s)):
            newList[indices[index]] = s[index]
            
        newString = ''.join(newList)
        
        return newString

    def restoreString1(self, s: str, indices: List[int]) -> str:
        
        newList = [0] * len(s)
        
        for index, letter in zip(indices, s):
            newList[index] = letter
            
        return ''.join(newList)