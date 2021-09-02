# Leetcode # 1844 
# https://leetcode.com/problems/replace-all-digits-with-characters/
# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

def replaceDigits(s):
            
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    newS = ''
    
    for index in range(0, len(s)-1, 2):
        newS += s[index]
        currentCharIndex = letters.index(s[index])
        if currentCharIndex < 25:
            newS += letters[currentCharIndex + int(s[index+1])]
        else:
            newS += "z"
            
    if len(s) % 2 == 1:
        newS += s[-1]
        
    return newS

#* This solution uses ordinal(ord) and character(chr)
def replaceDigits(s):
        
    newS = ''
    
    for index in range(0, len(s)-1, 2):
        newS += s[index] + chr(ord(s[index]) + int(s[index+1]))
            
    if len(s) % 2 == 1:
        newS += s[-1]
        
    return newS