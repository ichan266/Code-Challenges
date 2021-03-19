# LeetCode #953
def isAlienSorted(words: list[str], order: str) -> bool:

    ORDER = list(order)

    def checkOrder(word1, word2):
        for index in range(min(len(word1), len(word2))):
            i1 = ORDER.index(word1[index])
            i2 = ORDER.index(word2[index])
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


print(isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
