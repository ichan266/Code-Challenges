def kthLargestElement(nums, k):
    """ Given a list and a number, k, find the k-th largest element from the list without using indexing into the list (i.e. Use Stacks & Queues)."""

    newList = [nums[0]]
    tempList = []

    for idx in range(1, len(nums)):
        firstNum = newList[0]
        lastNum = newList[-1]
        if nums[idx] >= lastNum:
            newList.append(nums[idx])
        elif nums[idx] <= firstNum:
            newList.insert(0, nums[idx])
        else:
            while nums[idx] < newList[-1]:
                tempList.append(newList.pop())
            newList.append(nums[idx])
            tempList.reverse()
            newList.extend(tempList)
            tempList = []

    return newList[len(nums)-k]


print(kthLargestElement([3, 2, 1, 5, 6, 4], 2))
ls = [3, 2, 1, 5, 6, 4]
