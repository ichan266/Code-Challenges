# LeetCode Problem #1323
def maximum69Number (num: int) -> int:
        
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

num=6969
print(maximum69Number(num))