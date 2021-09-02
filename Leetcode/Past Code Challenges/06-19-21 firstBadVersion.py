# Leetcode # 278
# Easy
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def firstBadVersion(n):
    left = 0
    right = n

    while right > left:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left
