# Leetcode # 1002
# https://leetcode.com/problems/find-common-characters/
# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

import collections

def commonChars(A):
    
    result = []
    
    test = collections.Counter(A[0])
    
    for index in range(1, len(A)):
        current = collections.Counter(A[index])
        if test != current:
            temp = {}
            for key, value in current.items():
                if key in test:
                    if test[key] == value:
                        temp[key] = value
                    else:
                        temp[key] = min(test[key], value)
            test = temp

    for key, value in test.items():
        for _ in range(value):
            result.append(key)

    return result