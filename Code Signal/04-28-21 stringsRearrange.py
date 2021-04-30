# Code Signal Arcade #33
def stringsRearrangement(inputArray):

    def checkStr(a, b):
        return 1 == sum([i != j for i, j in zip(a, b)])

    indexDict = {i: [] for i in range(len(inputArray))}

    for i in range(len(inputArray)):
        for j in range(i+1, len(inputArray)):
            if checkStr(inputArray[i], inputArray[j]):
                indexDict[i].append(j)
                indexDict[j].append(i)

    # quick little short circuit. If there are any strings that can't
    # be adjacent to other strings, there's no ordering that works.
    for item in indexDict.values():
        if item == []:
            return False

    # current: index of the string we're currently on
    # remaining: list of valid indices we can still use
    def visit(current, remaining):
        remaining.remove(current)

        # if all of the positions have been visited, we've reached a valid
        # solution.
        if (remaining == []):
            return True

        # visit all of the reachable positions from current
        # that haven't already been visited
        for i in indexDict[current]:
            if (i in remaining):
                if (visit(i, remaining)):
                    return True

        # if we didn't find a valid result after testing all strings that
        # could follow this one, there's no answer on this particular
        # "path", so out the current value back in the list and return false
        # to continue the search.
        remaining.append(current)
        return False

    # Any position could be a valid starting point, so start by testing each as
    # the first item in the list.
    allPositions = [i for i in range(len(inputArray))]
    for i in range(len(inputArray)):
        if visit(i, allPositions):
            return True

    return False
