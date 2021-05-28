# Leetcode #504
# https://leetcode.com/problems/base-7/

# Given an integer num, return a string of its base 7 representation.

def convertToBase7(num):

    if num == 0:
        return "0"

    negative = False

    if num < 0:
        num = abs(num)
        negative = True

    resultStr = ''

    while num:
        div, mod = divmod(num, 7)
        num = div
        resultStr += chr(ord("0") + mod)

    if negative:
        return "-" + resultStr[::-1]

    return resultStr[::-1]

# % Discussion
# % This is a bit of a mathy questions. The very first step is to check if num == 0, which we can just return "0". This step is necessary since we are using num's value in our while loop. Next step is to check if num is negative. If it is, we change negative from False to True (will use this to add "-" back to our answer when we are done with the algorithm. See line 24). We then change this num back to positive in order to process it correctly (reason: -1//7 = -1). To convert any based-10 number to a different base, we need to use divmod operation. (div gives you result from floored division while mod give you result from modulus). So the general idea is:
# % eg. num == 1000
# %                     Div     Mod
# % Step 1: 1000 // 7   142     6   -> num = div = 142
# % Step 2: 142 // 7    20      2   -> num = div = 20
# % Step 3: 20 // 7     2       6   -> num = div = 2
# % Step 4: 2 //7       0       2   -> num = div = 0
# % Step 5: break out of while loop since num is now 0

# % We initialize the empty string, resultStr. And we keep adding mod to the string by converting the result from mod to str using ordinal as we go.
# % Final steps are to check if it is negative, then reverse the string when we return it.
