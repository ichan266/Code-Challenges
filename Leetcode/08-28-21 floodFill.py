# Leetcode # 733
# Flood Fill - 2D arrays, Recursion
# Easy
# https://leetcode.com/problems/flood-fill/

def floodFill(image, sr, sc, newColor):

    if image[sr][sc] == newColor:
        return image

    currentValue = image[sr][sc]
    image[sr][sc] = newColor

    # Neighboring cells positions in tuple, with 1st value==row and 2nd value==column
    top = (sr-1, sc) if sr > 0 else None
    bottom = (sr + 1, sc) if sr < len(image)-1 else None
    left = (sr, sc - 1) if sc > 0 else None
    right = (sr, sc + 1) if sc < len(image[0])-1 else None

    neighboringCells = [cell for cell in [top, bottom, left, right] if cell]

    for cell in neighboringCells:
        if image[cell[0]][cell[1]] == currentValue:
            floodFill(image, cell[0], cell[1], newColor)

    return image
