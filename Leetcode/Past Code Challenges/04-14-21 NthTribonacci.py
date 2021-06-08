# Leetcod #1137
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

import timeit
class Solution:

    cache = {}
    
    #* This solution is by Natasha. Please note that the cache must be started outside of the main function in order to stay under "Time Limit Exceeded"
    def tribonacci1(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else: 
            if n not in self.cache:
                self.cache[n] = self.tribonacci1(n-3) + self.tribonacci1(n-2) + self.tribonacci1(n-1)
        
        return self.cache[n]

    #@ This is my answer but it hit "Time Limit Exceeded"
    def tribonacci2(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        return self.tribonacci2(n-3) + self.tribonacci2(n-2) + self.tribonacci2(n-1)

    # % Master Ben's solution
    def tribonacci3(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        array = [0, 1, 1]
        
        for idx in range(3, n+1):
            array.append(array[idx-3] + array[idx-2] + array[idx-1])
            
        return array[n]

    def tribonacci4(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        array = [0] * (n+1)
        array[1], array[2] = 1, 1
        
        for idx in range(3, n+1):
            array[idx] = array[idx-3] + array[idx-2] + array[idx-1]
            
        return array[n]

instance = Solution()

#print(timeit.timeit(lambda:instance.tribonacci2(20), number=10))
print(timeit.timeit(lambda:instance.tribonacci1(2000), number=10))
print(timeit.timeit(lambda:instance.tribonacci3(2000), number=10))
print(timeit.timeit(lambda:instance.tribonacci4(2000), number=10))

# print(instance.tribonacci3(400))
# print(instance.tribonacci4(400))
# print(instance.tribonacci2(25))