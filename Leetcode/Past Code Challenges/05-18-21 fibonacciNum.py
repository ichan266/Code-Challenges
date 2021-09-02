# Leetcode # 509
# https://leetcode.com/problems/fibonacci-number/

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n)

def fib(n: int) -> int:

    a, b = 0, 1
    result = 0

    for _ in range(n):
        result = a + b
        a = b
        b = result

    return a
