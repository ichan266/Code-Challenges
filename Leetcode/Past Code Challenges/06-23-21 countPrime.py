# Leetcode # 204
# Easy (but not really...)
# https://leetcode.com/problems/count-primes/

# Count the number of prime numbers less than a non-negative number, n.

import math


def countPrimes(n):

    if (n < 2):
        return 0

    results = [True]*n
    results[0] = False
    results[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        # if i is still prime, it's prime
        # mark its multiples as not prime
        if results[i]:
            for j in range(2*i, n, i):
                results[j] = False

    return results.count(True)
