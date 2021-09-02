# Leetcode # 405
# Easy
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

# Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
# Note: You are not allowed to use any built-in library method to directly solve this problem.

# This is my solution, which only works for positive numbers
def toHex1(num):
    hexDigit = "0123456789abcdef"

    result = ""

    while True:
        div, mod = divmod(num, 16)
        result = hexDigit[mod] + result
        if div > 16:
            num = div
            continue
        else:
            result = hexDigit[div] + result
            break

    return result


# @ Pair Programming with Ben: This one works for -1 with expected result = "ffffffff"
def toHex2(num):
    hexDigit = "0123456789abcdef"

    result = ""

    for i in range(8):
        # div, mod = divmod(num, 16)
        result = hexDigit[num & 15] + result
        num = num >> 4
        if num == 0:
            break

    return result
