# Leetcod #1137
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

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
                self.cache[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        
        return self.cache[n]

    #@ This is my answer but it hit "Time Limit Exceeded"
    def tribonacci2(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        return self.tribonacci2(n-3) + self.tribonacci2(n-2) + self.tribonacci2(n-1)


instance = Solution()

print(instance.tribonacci2(4))
print(instance.tribonacci2(25))