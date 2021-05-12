# Code Signal Arcade #50

def chessKnight(cell):

    numInBound = {2, 3, 4, 5}

    x, y = ord(cell[0])-ord("a"), ord(cell[1])-ord("1")

    totalScore = 8
    hclip, vclip = 0, 0
    if x not in numInBound:
        hclip = min(abs(2-x), abs(5-x))*2

    if y not in numInBound:
        vclip = min(abs(2-y), abs(5-y))*2

    totalScore -= (hclip + vclip)
    if (hclip + vclip) == 8:
        totalScore += 2
    if (hclip + vclip) == 6:
        totalScore += 1

    return totalScore
