# Leetcode # 1839
# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
import re


def longestBeautifulSubstring1(word):

    vowels = list("aeiou")
    i = 0
    bestScore = 0

    while i < len(word):
        if word[i] == vowels[0]:
            currentScore = 0
            for pos in range(len(vowels)):
                if i >= len(word):
                    break
                elif word[i] != vowels[pos]:
                    i -= 1
                    break
                while i < len(word) and word[i] == vowels[pos]:
                    currentScore += 1
                    i += 1
            else:
                if pos == 4 and currentScore > bestScore:
                    bestScore = currentScore
                    i -= 1
        i += 1

        return bestScore


# * This one uses regex. It exceeds runtime limit but it will work
def longestBeautifulSubstring2(word):

    result = re.findall(r"a+e+i+o+u+", word)

    return len(max(result))


# @ This one is done by Ben
def longestBeautifulSubstring3(word):

    vowels = list("aeiou")
    bestScore = 0
    vowel_count = len(vowels)
    currentVowel = vowel_count
    currentScore = 0

    for letter in word:
        if currentVowel < vowel_count and letter == vowels[currentVowel]:
            currentScore += 1
            continue
        elif currentVowel+1 < vowel_count and letter == vowels[currentVowel+1]:
            currentScore += 1
            currentVowel += 1
            continue
        else:
            if currentVowel == vowel_count - 1 and currentScore > bestScore:
                bestScore = currentScore
            currentVowel = vowel_count
            currentScore = 0

        if currentVowel == vowel_count and letter == vowels[0]:
            if currentVowel != 0:
                currentScore = 1
                currentVowel = 0

    if currentVowel == vowel_count - 1 and currentScore > bestScore:
        bestScore = currentScore

    return bestScore
