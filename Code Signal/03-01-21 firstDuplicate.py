def firstDuplicate(a):

    numSet = set()

    for num in a:
        if num not in numSet:
            numSet.add(num)
        else:
            return num

    return -1

print(firstDuplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8]))
ls = [1, 2, 3, 3]


## Given a list of elements, find its negative index in the List. ##
def negIndex(ls, K):

    print(f"length is {len(ls)}")

    return -(len(ls)-ls.index(K))

print(negIndex([5, 7, 8, 2, 3, 5, 2, 1], K = 2 ))
