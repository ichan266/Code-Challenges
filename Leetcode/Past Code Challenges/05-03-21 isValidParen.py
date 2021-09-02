# Leetcode #20
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def isValid(s):
    
    openingSet = set("([{")
    closingDict = {")": "(", "]": "[", "}": "{"}
    
    trackingList = []
    
    for char in s:
        if char in openingSet:
            trackingList.append(char)
        if char in closingDict:
            if trackingList == [] or closingDict[char] != trackingList[-1]:
                return False
            else:
                trackingList.pop()
                
    return trackingList == []