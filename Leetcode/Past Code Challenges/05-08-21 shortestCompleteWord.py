# Leetcode #748
# https://leetcode.com/problems/shortest-completing-word/
# Given a string licensePlate and an array of strings words, find the shortest completing word in words.

# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

def shortestCompletingWord(licensePlate, words):

    letters = [char.lower() for char in licensePlate if char.isalpha()]

    lettersDict = {}

    for letter in letters:
        lettersDict[letter] = lettersDict.get(letter, 0) + 1

    result = []

    for word in words:
        tempDict = {}
        for letter in word:
            if letter in lettersDict:
                tempDict[letter] = tempDict.get(letter, 0) + 1
                if tempDict[letter] > lettersDict[letter]:
                    tempDict[letter] = lettersDict[letter]
        if tempDict == lettersDict:
            result.append(word)

    result.sort(key=lambda x: len(x))

    return result[0]
