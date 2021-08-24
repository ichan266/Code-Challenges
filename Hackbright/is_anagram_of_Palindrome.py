# Given a word, determind if the given word is a re-scrambling of palindrome
# Challenge: Easy
# Whiteboard: Medium

import collections


def is_anagram_of_Palindrome(string):
    sDict = collections.Counter(string)
    odd = 0

    for count in sDict.values():
        if count % 2 == 1:
            odd += 1
            if odd > 1:
                return False

    return True


print(is_anagram_of_Palindrome("arceaceb"))
