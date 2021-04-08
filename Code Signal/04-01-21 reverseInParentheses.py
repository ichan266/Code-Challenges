# Write a function that reverses characters in (possibly nested) parentheses in the input string.
def reverseInParentheses(inputString):

    def findCharInBracket(inputStr):
        for idx in range(len(inputStr)):
            if inputStr[idx] == "(":
                startIdx = idx
            elif inputStr[idx] == ")":
                stopIdx = idx - 1
                break

        reversed = inputStr[stopIdx:startIdx:-1]

        return inputStr[:startIdx] + reversed + inputStr[stopIdx + 2:]

    while ")" in inputString:
        inputString = findCharInBracket(inputString)

    return inputString


# % This one is from another user. Need to think about it...
def reverseInParentheses1(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
