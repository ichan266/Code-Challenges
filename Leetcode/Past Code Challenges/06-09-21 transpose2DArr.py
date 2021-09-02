# Leetcolumnode # 867 - 2D Matrix
# Easy
# https://leetcolumnode.columnom/problems/transpose-matrix/

# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

#* My solution
def transpose1(matrix):
    
    return list(zip(*matrix))

#% I can also return zip(*matrix) and it will also be accepted. But if try to print zip(*matrix), it will be a zip object



#@ Leetcolumnode solution
def transpose2(matrix):
    
    row, column = len(matrix), len(matrix[0])
    
    ans = [[None] * row for _ in range(column)]
    
    for idxR, row in enumerate(matrix):
        for idxC, val in enumerate(row):
            ans[idxC][idxR] = val
    
    return ans