# Leetcode # 925
# Long Pressed Name
# Easy
# https://leetcode.com/problems/long-pressed-name/

from itertools import groupby


def isLongPressedName(name: str, typed: str) -> bool:

    pos = 0
    for idx in range(len(name)):
        # are we at the end of typed but still have more input?
        if pos == len(typed):
            return False
        # Do we have a matching character for the current name char?
        if name[idx] != typed[pos]:
            return False
        pos += 1
        # If at end of name or next char is different, eat any extra duplicates in typed
        if idx == len(name)-1 or name[idx] != name[idx+1]:
            while pos < len(typed) and typed[pos] == name[idx]:
                pos += 1

    return pos == len(typed)


def isLongPressedName1(name: str, typed: str) -> bool:

    # groupby name and typed
    name = [(i, len(list(v))) for i, v in groupby(name)]

    typed = [(i, len(list(v))) for i, v in groupby(typed)]

    # mismatched groups
    if len(name) != len(typed):
        return False

    # iterate through name:
    for i, v in enumerate(name):

        # wrong letter
        if name[i][0] != typed[i][0]:
            return False

        # not enough letter
        if name[i][1] > typed[i][1]:
            return False

    return True
