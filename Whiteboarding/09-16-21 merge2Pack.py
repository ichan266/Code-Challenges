def get_indices_of_item_wights1(arr, limit):

    answer = []

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == limit:
                answer = [j, i]

    return answer


def get_indices_of_item_wights2(arr, limit):

    arrDict = {}

    for i in range(len(arr)):
        wt = arr[i]
        target = limit - arr[i]
        if target in arrDict:
            return [i, arrDict[target]]
        else:
            arrDict[wt] = i

    return []
