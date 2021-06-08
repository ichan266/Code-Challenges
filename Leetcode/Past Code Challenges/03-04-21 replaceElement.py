# Leetcode #1299
def replaceElements(arr):
    """Given an array, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1."""
    
    length = len(arr)
    
    if length == 1:
        return [-1]
    
    result = []
    
    for index, _ in enumerate(arr):
        while len(arr) > 1:
            maxRight = max(arr[index+1:])
            result.append(maxRight)
            arr = arr[index+1:]
    
    result.append(-1)
    
    return result

print(replaceElements([17,18,5,4,6,1]))