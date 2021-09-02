# Leetcode # 5
# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.

def longestPalindrome(s):

    def longestFromPos(char, lpos, rpos):

        longest = char

        while (lpos >= 0 and rpos < len(s)) and s[lpos] == s[rpos]:
            longest = s[lpos:rpos+1]
            lpos -= 1
            rpos += 1

        return longest

    longestString = s[0]

    for i in range(len(s)-1):
        result = longestFromPos(s[i], i, i+1)
        if len(result) > len(longestString):
            longestString = result
        result = longestFromPos(s[i], i-1, i+1)
        if len(result) > len(longestString):
            longestString = result

    return longestString
