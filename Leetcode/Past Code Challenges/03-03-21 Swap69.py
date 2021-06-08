# LeetCode Problem #1323
def maximum69Number (num: int) -> int:
    """Given an integer contains only 6's & 9's, you may check up to one digit to maximize the number."""
        
    numCopy = num
    numOfDigit = 0

    while numCopy:
        numCopy = numCopy // 10
        numOfDigit += 1

    result = 0
    power = numOfDigit-1

    for _ in range(numOfDigit):
        currentDigit = num // (10 ** power)
        currentNum = currentDigit * (10 ** power)
        if currentDigit == 6:
            currentDigit = 9
            currentNum = currentDigit * (10 ** power)
            result += currentNum
            num = num % (6*(10**power)) 
            break
        else:
            result += currentNum
            num -= currentNum
            power -= 1

    return result + num


def maximum69Number2 (num: int) -> int:

    numStr = str(num)
    
    result = ''

    for index, digitStr in enumerate(numStr):
        if digitStr == "6":
            digitStr = "9"
            result += digitStr + numStr[index+1:]
            break
        result += digitStr

    return int(result)

num=6969
print(maximum69Number2(num))