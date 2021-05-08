# Leetcode # 1566
# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
# Given an array of positive integers arr,  find a pattern of length m that is repeated k or more times.

# A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

# Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.


def containsPattern(arr, m, k):

    for index1 in range(len(arr)-(m*k)+1):
        currentPattern = arr[index1:index1+m]
        for index2 in range(index1+m, index1+(m*k), m):
            nextPattern = arr[index2:index2+m]
            if (currentPattern != nextPattern):
                break
        else:
            return True
    return False

# % Note that this solution was done with Ben.

# % `for index1 in range(len(arr)-(m*k)+1)`
# % Reason to use m*k is because the pattern is m length and needs to occur kth time. So we can stop before m*k because if we are up to that point and still haven't found the pattern, there will not be enough character to match the pattern kth time
