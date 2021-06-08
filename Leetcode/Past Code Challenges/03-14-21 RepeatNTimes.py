# Leetcode #961
def repeatedNTimes(A) -> int:
    """ In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times."""

    N = len(A)/2
    charCount = {}

    for char in A:
        charCount[char] = charCount.get(char, 0) + 1
        if charCount[char] == N:
            return char
