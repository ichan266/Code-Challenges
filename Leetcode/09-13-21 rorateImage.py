# Leetcode # 48
# Rotate Image
# Medium
# https://leetcode.com/problems/rotate-image/

# V1: I am not supposed to use an additional data structure. So this solution works but very slowly. Also, it did not meet the criteria of not using extra data structure


def rotate1(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    result = []

    for i in zip(*matrix):
        result.append(i[::-1])

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = result[row][col]


def rotate2(matrix):

    end = len(matrix) - 1

    for row in range(len(matrix) // 2):
        for col in range((len(matrix) + 1) // 2):
            a = matrix[row][col]
            b = matrix[col][end-row]
            c = matrix[end-row][end-col]
            d = matrix[end-col][row]
            matrix[row][col] = d
            matrix[col][end-row] = a
            matrix[end-row][end-col] = b
            matrix[end-col][row] = c
