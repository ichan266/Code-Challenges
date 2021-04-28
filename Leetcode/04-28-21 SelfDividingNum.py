# Leetcode #728
# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

from typing import List


class Solution:
    def selfDividingNumbers1(self, left: int, right: int) -> List[int]:

        def isSelfDividing(num):

            for digit in str(num):
                if digit == "0" or num % int(digit) != 0:
                    return False

            return True

        selfDividingNumList = []

        for i in range(left, right+1):
            if isSelfDividing(i):
                selfDividingNumList.append(i)

        return selfDividingNumList

    # % This one uses Python built-In divmod function
    def selfDividingNumbers2(self, left: int, right: int) -> List[int]:

        def isSelfDividing(num):

            temp = num

            while temp > 0:
                temp, digit = divmod(temp, 10)
                if digit == 0 or num % digit != 0:
                    return False

            return True

        selfDividingNumList = []

        for i in range(left, right+1):
            if isSelfDividing(i):
                selfDividingNumList.append(i)

        return selfDividingNumList


instance = Solution()

print(instance.selfDividingNumbers2(1, 22))
