# Leetcode # 1346
# Check If N and Its Double Exist
# This is the question I gave Monisha

# * My solution
def checkIfExist(arr: list[int]) -> bool:

    valueDict = {value: index for index, value in enumerate(arr)}

    for index in range(len(arr)):
        key = arr[index]*2
        if key in valueDict and valueDict[key] != index:
            return True

    return False


# @ Solution with Set
def checkIfExist(arr: list[int]) -> bool:

    if arr.count(0) > 1:
        return True

    valueSet = set(arr)

    for value in valueSet:
        if value != 0 and value*2 in valueSet:
            return True

    return False
