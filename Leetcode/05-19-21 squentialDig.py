# Leetcode # 1291
# https://leetcode.com/problems/sequential-digits/

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

def sequentialDigits(low: int, high: int) -> list[int]:

    digitList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    lowLen = len(str(low))
    highLen = len(str(high))

    result = []

    for idx in range(lowLen, highLen+1):
        for i in range(len(digitList)-idx+1):
            num = int(''.join(digitList[i:i+idx]))
            if low <= num <= high:
                result.append(num)

    return result

    # def iterNum(length):
    #     iterNum = 0

    #     for i in range(length):
    #         iterNum = (iterNum*10) + 1

    #     return iterNum

    # def startNum(low):
    #     length = len(str(low))
    #     iterN = iterNum(length)
    #     firstDigitIndex = digitList.index(str(low)[0])
    #     startNum = int(
    #         ''.join(digitList[firstDigitIndex:firstDigitIndex+length]))

    #     if startNum < low:
    #         return startNum + iterN

    #     return startNum
