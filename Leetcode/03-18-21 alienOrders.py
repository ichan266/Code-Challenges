# LeetCode #953
def isAlienSorted(words: List[str], order: str) -> bool:

    aliensOrder = list(order)

    def checkOrder(word1, word2):
        for index in range(min(len(word1), len(word2))):
            i1 = aliensOrder.index(word1[index])
            i2 = aliensOrder.index(word2[index])
            if i1 > i2:
                return False
            elif i1 < i2:
                return True

        if len(word1) > len(word2):
            return False

        return True

    for index in range(len(words)-1):
        if checkOrder(words[index], words[index+1]) == False:
            return False

    return True
