# Leetcode # 1925
# Easy
# https://leetcode.com/problems/count-square-sum-triples/

from math import sqrt


def countTriples(n: int) -> int:

    count = 0
    numSet = set(num * num for num in range(1, n+1))

    for num1 in range(3, n+1):
        for num2 in range(n, 2, -1):
            if ((num1*num1) + (num2*num2)) in numSet:
                count += 1

    return count


def countTriplesSqrt(n: int) -> int:

    count = 0
    bSet = set(num * num for num in range(1, n+1))

    for c in range(3, n+1):
        stop = int(sqrt((c*c)/2))
        for a in range(3, stop+1):
            if ((c*c) - (a*a)) in bSet:
                count += 2

    return count
