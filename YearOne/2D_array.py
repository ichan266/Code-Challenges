"""
We are designing a 2D game and we have a game map that we represent by an integer matrix. For now, each cell can be a wall (denoted by -1) or a blank space (0).

board = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]

The player can move 1 space at a time up, down, left, or right. The player can't go through walls or land on a wall, or go through the edges of the board.

Write a function that, given a board and a player starting position (represented as a row-column pair), returns all of the possible next positions for the player.

Sample inputs (board, starting_position) and outputs (in any order):

findLegalMoves(board, (1, 1)) =>
  (0, 1), (1, 0)

findLegalMoves(board, (5, 3)) =>
  (5, 2), (5, 4), (4, 3), (6, 3)

findLegalMoves(board, (5, 1)) =>
  (6, 1), (4, 1), (5, 0), (5, 2)

findLegalMoves(board, (6, 0)) =>
  (5, 0), (6, 1)

findLegalMoves(board, (6, 4)) =>
  (5, 4), (6, 3)

findLegalMoves(board, (0, 0)) =>
  (0, 1), (1, 0)

findLegalMoves(board, (2, 2)) =>
  [empty]

n: width of the input board
m: height of the input board

"""

"""
Given a board and an end position for the player, write a function to determine if it is possible to travel from every open cell on the board to the given end position.

board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

board2 = [
    [  0,  0,  0, 0, -1 ],
    [  0, -1, -1, 0,  0 ],
    [  0,  0,  0, 0,  0 ],
    [ -1, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
]

board3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]

board4 = [
    [0,  0,  0,  0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0,  0,  0,  0, 0],
]

board5 = [
    [0],
]

end1 = (0, 0)
end2 = (5, 0)

Expected output:

isReachable(board1, end1) -> True
isReachable(board1, end2) -> True
isReachable(board2, end1) -> False
isReachable(board2, end2) -> False
isReachable(board3, end1) -> False
isReachable(board4, end1) -> True
isReachable(board5, end1) -> True
"""
"""
board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

board2 = [
    [  0,  0,  0, 0, -1 ],
    [  0, -1, -1, 0,  0 ],
    [  0,  0,  0, 0,  0 ],
    [ -1, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
]

board3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]

board4 = [
    [ 0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, 0 ],
    [ 0, -1, -1, -1, 0 ],
    [ 0, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0, 0 ],
]

board5 = [
    [ 0 ],
]

end1 = (0, 0)
end2 = (5, 0)
"""

"""
Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0. The image you get is known to have a single rectangle of 0s on a background of 1s.

Write a function that takes in the image and returns one of the following representations of the rectangle of 0's: top-left coordinate and bottom-right coordinate OR top-left coordinate, width, and height.

image1 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1],
]

Sample output variations (only one is necessary):

findRectangle(image1) =>
  x: 3, y: 2, width: 3, height: 2
  2,3 3,5 -- row,column of the top-left and bottom-right corners

"""
"""image1 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1],
]

image2 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]

image3 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 0, 0],
  [1, 1, 1, 1, 1, 0, 0],
]

image4 = [
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
]

image5 = [
  [0],
]
"""


"""
Your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
	['c', 'c', 'c', 'a', 'r', 's'],
	['c', 'c', 'i', 't', 'n', 'b'],
	['a', 'c', 'n', 'n', 't', 'i'],
	['t', 'c', 'i', 'i', 'p', 't']
]

word1_1 = "catnip"
find_word_location(grid1, word1_1)-> [ (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4) ]

word1_2 = "cccc"
find_word_location(grid1, word1_2)-> [(0, 1), (1, 1), (2, 1), (3, 1)]
OR [(0, 0), (1, 0), (1, 1), (2, 1)]
OR [(0, 0), (0, 1), (1, 1), (2, 1)]
OR [(1, 0), (1, 1), (2, 1), (3, 1)]


grid2 = [
    ['c', 'p', 'a', 'n', 't', 's'],
    ['a', 'b', 'i', 't', 'a', 'b'],
    ['t', 'f', 'n', 'n', 'c', 'i'],
    ['x', 's', 'c', 'a', 't', 'n'],
    ['x', 's', 'd', 'd', 'e', 'a'],
    ['s', 'q', 'w', 'x', 's', 'p']
]


word2 = "catnap"
find_word_location(grid2, word2)-> [ (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5) ]

grid3 = [
    ['c', 'r', 'c', 'a', 'r', 's'],
    ['a', 'b', 'i', 't', 'n', 'i'],
    ['t', 'f', 'n', 'n', 'x', 'p'],
    ['x', 's', 'i', 'x', 'p', 't']]
word3 = "catnip"
find_word_location(grid3, word3)-> [ (0, 2), (0, 3), (1, 3), (1, 4), (1, 5), (2, 5) ]

n = number of rows
m = number of columns
w = length of the word
"""