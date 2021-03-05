def minion_game(string):
    vowels = set("AEIOU")
#!  This one doesn't work!!!
#    Stuart has to make words starting with consonants.
#    Kevin has to make words starting with vowels.

#    if not string:
#        print("Draw")
#        return

#    stuart_words_count = {}
#    kevin_words_count = {}

#    Stuart
#    for index, letter in enumerate(string):
#        if letter not in vowels:
#            current_word = string[index:]
#            for _ in range(len(current_word)):
#                stuart_words_count[current_word] = stuart_words_count.get(current_word, 0) + 1
#                current_word = current_word[:-1]

#    Kevin
#    for index, letter in enumerate(string):
#        if letter in vowels:
#            current_word = string[index:]
#            for _ in range(len(current_word)):
#                kevin_words_count[current_word] = kevin_words_count.get(current_word, 0) + 1
#                current_word = current_word[:-1]

#    stuart_score = sum(stuart_words_count.values())
#    kevin_score = sum(kevin_words_count.values())

#    if stuart_score > kevin_score:
#        print(f"Stuart {stuart_score}")
#    elif stuart_score < kevin_score:
#        print(f"Kevin {kevin_score}")
#    else:
#        print("Draw")

    stuartScore = 0
    kevinScore = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevinScore += len(string)-i
        else:
            stuartScore += len(string)-i

    if stuartScore > kevinScore:
        print(f"Stuart {stuartScore}")
    elif stuartScore < kevinScore:
        print(f"Kevin {kevinScore}")
    else:
        print("Draw")


print(minion_game("BANANA"))
