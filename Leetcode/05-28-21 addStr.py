# Leetcode # 415
# https://leetcode.com/problems/add-strings/

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

#% Solution 1: This will convert both numbers into integers, calculate sum, then convert it back to string. This has very slow runtime, probably because of steps taken to convert the numbers to integers, then back to string.
def addStrings1(num1, num2):
    
    def convertStrToInt(numStr):
        result = 0
        for digit in numStr:
            result = (result * 10) + (ord(digit) - ord("0"))
        return result
    
    resInt = convertStrToInt(num1) + convertStrToInt(num2)
    
    if resInt == 0:
        return "0"
    
    resStr = ''
    
    while resInt:
        resStr += chr(ord("0") + (resInt % 10))
        resInt //= 10
        
    return resStr[::-1]


#% Solution 2: Using zip_longest in itertools, I get the digits from num1 and num2 at the same time, starting from their back. Note that at the time of zipping them, they are still strings, so the fillvalue will also need to be a string in order for the ordinal operation at line 39 to work when calculating res. We add the result to resStr as we go. Then return resStr[::-1] at the end since we are adding it "backwards"
def addStrings2(num1, num2):
    import itertools

    resStr = ''
    carry = 0

    for digit1, digit2 in itertools.zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
        res = (ord(digit1) - ord("0")) + (ord(digit2) - ord("0")) + carry
        if res >= 10:
            carry = 1
            res = res - 10
        else:
            carry = 0
        resStr += chr(ord("0") + res)
        
    if carry:
        resStr += "1"

    return resStr[::-1]