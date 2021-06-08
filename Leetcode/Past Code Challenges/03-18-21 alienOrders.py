# LeetCode #953
def checkOrder(ORDERED_DICT, word1, word2):
    for index in range(min(len(word1), len(word2))):
        i1 = ORDERED_DICT[word1[index]]
        i2 = ORDERED_DICT[word2[index]]
        if i1 > i2:
            return False
        elif i1 < i2:
            return True

    if len(word1) > len(word2):
        return False

    return True


def isAlienSorted(words: list[str], order: str) -> bool:

    ORDERED_DICT = {value: key for key, value in enumerate(order)}

    for index in range(len(words)-1):
        if checkOrder(ORDERED_DICT, words[index], words[index+1]) == False:
            return False

    return True


print(isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
