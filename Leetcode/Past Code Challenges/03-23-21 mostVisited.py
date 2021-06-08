# LeetCode #1560
def mostVisited(n, rounds):

    first = rounds[0]
    last = rounds[-1]

    if first < last:
        return [i for i in range(first, last + 1)]
    elif first > last:
        biggerList = [i for i in range(first, n + 1)]
        smallerList = [i for i in range(1, last + 1)]
        return smallerList + biggerList
    else:
        return [first]

# % Discussion
# @ This is a bit of a tricky question because we actually don't care how many times it
# @ circles. All we care is the first number and the last number in the list.
# @ We will visit all the sectors when we run through it once. So we really don't
# @ need to count them as we move though the circle. We only need to know where it
# @ starts and where it stops.

# @ If the first number is smaller than the last one, we just need to get a range of
# @ every number between them (i.e. range(first, last+1))

# @ If the first number is greater than the last one, then we will need to split the
# @ list, with the first (and bigger) number as start of the bigger list, running all
# @ the way to n+1: (range(first, n+1)); while with the last (and smaller) number as
# @ the end of smaller list, (range(1, last+1)). Then return smaller list + bigger list.

# @ Else (i.e. they are the same), then I can just put either number into a list and
# @ return it.
