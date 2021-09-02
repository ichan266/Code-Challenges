import itertools


def nextGreaterElement(n: int) -> int:

    # Convert all the digits to a list. It runs backwards
    nList = []
    while n:
        nList.append(n % 10)
        n //= 10

    # Helper function to convert list back to a number
    def digitsToNum(ls):
        ls = ls[::-1]
        num = 0
        for digit in ls:
            num = num*10 + digit
        return num

    pos1 = -1
    val1 = 0
    for idx, num in enumerate(nList[1:]):
        if num < nList[idx]:
            pos1 = idx+1
            val1 = num
            break
    else:
        return -1

    pos2 = -1
    val2 = None
    for idx, num in enumerate(nList[:pos1]):
        if num > val1 and (val2 == None or num < val2):
            pos2 = idx
            val2 = num

    nList[pos1], nList[pos2] = val2, val1

    result = nList[:pos1]
    result.sort(reverse=True)
    result.extend(nList[pos1:])

    finalAnswer = digitsToNum(result)
    if finalAnswer < 2**31:
        return finalAnswer
    else:
        return -1


def nextGreaterElementPerms(n: int) -> int:

    # Convert all the digits to a list. It runs backwards
    nList = []
    tmp = n
    while tmp:
        nList.append(tmp % 10)
        tmp //= 10

    # Helper function to convert list back to a number
    def digitsToNum(ls):
        ls = ls[::-1]
        num = 0
        for digit in ls:
            num = num*10 + digit
        return num

    perms = itertools.permutations(nList)
    result = digitsToNum(sorted(nList))
    for mList in perms:
        test = digitsToNum(mList)
        if n < test and test < result:
            result = test

    if result < 2**31 and result != n:
        return result
    else:
        return -1


print(f"Result = {nextGreaterElement(124312)}")
