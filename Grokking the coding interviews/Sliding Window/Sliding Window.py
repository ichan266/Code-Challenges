# Sliding Windows

# Brute Force
def arrKitemAverage1(arr, k):

    return [(sum(arr[i:i+k]))/k for i in range(len(arr)-k+1)]


# Sliding Window
def arrKitemAverage2(arr, k):

    total = sum(arr[:k])
    result = [total/k]

    for i in range(len(arr)-k):
        total = total - arr[i] + arr[i+k]
        result.append(total/k)

    return result


print(arrKitemAverage1([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
print(arrKitemAverage2([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
