# Leetcode # 646
# Medium
# https://leetcode.com/problems/maximum-length-of-pair-chain/

# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.

def findLongestChain(pairs):

    pairs = sorted(pairs, key=lambda x: x[1])

    total = 1
    current = pairs[0][1]

    for i in range(1, len(pairs)):
        if pairs[i][0] > current:
            total += 1
            current = pairs[i][1]

    return total
