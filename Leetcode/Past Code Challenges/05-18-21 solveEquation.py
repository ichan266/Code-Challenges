# Leetcode # 640
# https://leetcode.com/problems/solve-the-equation/

# Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.

# If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

import re


def solveEquation(equation: str) -> str:

    left, right = equation.split("=")
    leftNumList, rightNumList = re.findall(
        r'[-]?\d+\b(?!x)', left), re.findall(r'[-]?\d+\b(?!x)', right)
    leftXList, rightXList = re.findall(
        r'[-]?\d*?x', left), re.findall(r'[-]?\d*?x', right)

    finalNumResult = sum([int(num) for num in rightNumList]) - \
        sum([int(num) for num in leftNumList])

    def xValue(item):
        if len(item) == 1:
            return 1
        elif len(item) == 2 and item[0] == "-":
            return -1
        else:
            return int(item[:-1])

    leftXSum, rightXSum = 0, 0

    for itemL in leftXList:
        leftXSum += xValue(itemL)

    for itemR in rightXList:
        rightXSum += xValue(itemR)

    finalXResult = leftXSum - rightXSum

    if finalXResult == 0:
        return "Infinite solutions" if not finalNumResult else "No solution"

    return "x=" + str(finalNumResult//finalXResult)

# * Discussion
# * A very challenging question with lot of little details when using Regex to separate the numbers the x's.
# * The biggest challenge using Regex is trying to match numbers but without the x attached to it (e.g. 2x).
# * I had to using r'[-]?\d+\b(?!x)' with (?!x) is a negative look-ahead, meaning DO NOT match if a number is
# * followed by x.
# *
# * So the logic goes putting all the numbers on the right side by right side minus left side; then putting
# * all the values of x on the left side by left side value minus right side.
# *
# * The algorithm handling the answer was not as tricky as I thought: first, I check for cases we can't reach
# * a solution (i.e. Infinite solutions OR No solution). If not, in order to make x equal to 1, I just need to
# * divide both side by the value of x. It should work with all values.
# *
