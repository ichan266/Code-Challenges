# Leetcode # 1260
# https://leetcode.com/problems/shift-2d-grid/

# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

# In one shift operation:

# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

# % This solution "flatten" the 2D array to a simple array with no nested arrays, create a new array by
# % using the k value, counting elements from the back, and move k amount of elements to the front.
# % Final step was to recreate the 2D array based on # of column in the original 2D array
def shiftGrid1(grid, k):

    combined = [num for rows in grid for num in rows]

    if k > len(combined):
        k = k % len(combined)

    newList = combined[-k:] + combined[:-k]
    col = len(grid[0])

    return [newList[i:i+col] for i in range(0, len(newList), col)]


# @ Pair programming with Ben. General strategy is to shift forward instead of backward (see line 35: rows*cols is the total amount of items in the entire 2D array. Subtracting k % (rows*cols) will shift it forward)
def shiftGrid2(grid, k):

    rows = len(grid)
    cols = len(grid[0])

    k = (rows*cols) - (k % (rows*cols))

    return [[grid[(idxR + (k+idxC)//cols) % rows][(idxC + k % cols) % cols] for idxC in range(cols)] for idxR in range(rows)]
