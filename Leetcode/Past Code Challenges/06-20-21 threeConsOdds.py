# Leetcode # 1550
# Easy
# https://leetcode.com/problems/three-consecutive-odds/

# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

# * My version, using slicing
def threeConsecutiveOdds1(arr):

    for idx, num in enumerate(arr):
        if num % 2 == 1:
            checkArr = arr[idx+1:idx+3]
            if len(checkArr) < 2:
                return False
            for n in checkArr:
                if n % 2 == 0:
                    break
            else:
                return True

    return False


# @ Ben's optimized version using bitwise &. Very common pattern!
def threeConsecutiveOdds2(arr):

    run = 0
    for item in arr:
        if item & 1:
            run += 1
            if run == 3:
                return True
        else:
            run = 0
    return False
