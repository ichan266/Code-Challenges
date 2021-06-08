# Leetcode # 74
# https://leetcode.com/problems/search-a-2d-matrix/

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def searchMatrix(matrix, target):
    cols = len(matrix[0])
    left = 0
    right = (len(matrix) * len(matrix[0]))-1

    while True:
        mid = (left + right) // 2
        currentItem = matrix[mid//cols][mid % cols]
        if target == currentItem:
            return True
        elif left == right:
            return False
        elif target < currentItem:
            right = max(left, mid - 1)
        elif target > currentItem:
            left = min(right, mid + 1)
