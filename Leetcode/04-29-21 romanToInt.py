# Leetcode # 13

class Solution:
    def romanToInt(self, s: str) -> int:

        romanDict = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0

        index = 0

        while index < len(s)-1:
            current = romanDict[s[index]]
            next = romanDict[s[index+1]]
            if next > current:
                result += next - current
                index += 2
            else:
                result += current
                index += 1

        if index < len(s):
            result += romanDict[s[-1]]

        return result
