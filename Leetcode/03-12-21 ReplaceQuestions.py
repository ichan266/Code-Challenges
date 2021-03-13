# a and b == (!a) or (!b)

def modifyString(s: str) -> str:

    length = len(s)
    newS = ''

    for index in range(length):
        current = s[index]
        if current == "?":
            if (index == 0 or newS[-1] != "a") and (index == length - 1 or s[index+1] != "a"):
                current = "a"
            elif (index == 0 or newS[-1] != "b") and (index == length - 1 or s[index+1] != "b"):
                current = "b"
            else:
                current = "c"

        newS += current

    return newS


def modifyString1(s: str) -> str:

    length = len(s)
    newS = ''

    for index in range(length):
        current = s[index]
        if current == "?":
            # if the charcters before and after are not "a", use "a"
            #              if either is true, we can't use a
            #        [ is the previous character a  ]  or [ is the next character a                ]
            previous_is_a = (index > 0 and newS[-1] == "a")
            next_is_a = (index < length - 1 and s[index+1] == "a")
            previous_is_b = (index > 0 and newS[-1] == "b")
            next_is_b = (index < length - 1 and s[index+1] == "b")
            if not previous_is_a and not next_is_a:
                current = "a"
            elif not previous_is_b and not next_is_b:
                current = "b"
            else:
                current = "c"

        newS += current

    return newS


def modifyString2(s: str) -> str:

    # bounds checked compare character
    def is_character(s, index, char):
        if (index < 0):
            return False
        if (index >= len(s)):
            return False
        return s[index] == char

    length = len(s)
    newS = ''

    for index in range(length):
        current = s[index]
        if current == "?":
            if not is_character(newS, index-1, "a") and not is_character(s, index+1, "a"):
                current = "a"
            elif not is_character(newS, index-1, "b") and not is_character(s, index+1, "b"):
                current = "b"
            else:
                current = "c"

        newS += current

    return newS
