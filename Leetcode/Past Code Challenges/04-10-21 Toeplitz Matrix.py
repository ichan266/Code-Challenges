# Leetcode #766
# Given an m by n matrix, return True if the matrix is Toeplitz. Otherwise, return False.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

def isToeplitzMatrix(matrix) -> bool:
    for row in range(len(matrix)-1):
        for column in range(len(matrix[0])-1):
            if not matrix[row][column] == matrix[row+1][column+1]:
                return False

    return True


print(isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
print(isToeplitzMatrix([[1, 2], [2, 2]]))
