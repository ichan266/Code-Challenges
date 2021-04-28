# Code Signal Arcade
# Intro #24
# Solution from Ben
def minesweeper(matrix):

    width = len(matrix[0])
    height = len(matrix)

    # add current, one before, and one after
    def addRow(rowList, col):
        return sum(rowList[max(0, col-1):min(col+2, width)])

    def addSquare(row, col):
        count = 0
        for index in range(max(0, row-1), min(row+2, height)):
            count += addRow(matrix[index], col)
        return count

    def neighborCount(row, col):
        # count the 3x3 grid, subtract current square back out.
        return addSquare(row, col) - matrix[row][col]

    return [[neighborCount(row, col) for col in range(width)] for row in range(height)]

# From other user


def minesweeper1(matrix):

    r = []

    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i+x < len(matrix) and 0 <= j+y < len(matrix[0]):
                        l += matrix[i+x][j+y]

            r[i].append(l)
    return r
