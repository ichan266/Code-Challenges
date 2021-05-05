# Leetcode #1387 - Sort Integers By Power Value
# https://leetcode.com/problems/sort-integers-by-the-power-value/
# The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

# if x is even then x = x / 2
# if x is odd then x = 3 * x + 1
# For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

# Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

# Return the k-th integer in the range [lo, hi] sorted by the power value.

def getKth(lo, hi, k):
    
    powerValDict = {}
    
    for num in range(lo, hi+1):
        temp = num
        count = 0
        while num > 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = (num * 3) + 1
            count += 1
        powerValDict[count] = powerValDict.get(count, [])
        powerValDict[count].append(temp)
    
    sortWithPowerVal = sorted(powerValDict.items())
    
    result = []
    
    for item in sortWithPowerVal:
        result.extend(item[1])
        
    return result[k-1]

def getKth1(lo, hi, k):
    
    def sort(num):
        count = 0
        while num > 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = (num * 3) + 1
            count += 1
        return count
    
    result = sorted([num for num in range(lo, hi+1)], key=sort)
        
    return result[k-1]