# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# * My version #1. Not the cleanest one.
def max_sub_array_of_size_k1(k, arr):
    total, start = 0, 0
    subtotal = 0

    for end in range(len(arr)):
        if end < k:
            subtotal += arr[end]
            continue
        total = max(total, subtotal)
        subtotal = subtotal - arr[start] + arr[end]
        start += 1

    return max(total, subtotal)


# * My version #2. A little improvement
def max_sub_array_of_size_k2(k, arr):
    maxTotal = sum(arr[:k])
    subtotal = maxTotal

    for i in range(len(arr)-k):
        subtotal = subtotal - arr[i] + arr[i+k]
        maxTotal = max(maxTotal, subtotal)

    return maxTotal


# * Their version
def max_sub_array_of_size_k3(k, arr):
    max_sum, window_sum = 0, 0
    start = 0

    for end in range(len(arr)):
        window_sum += arr[end]
        if end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1

    return max_sum


print(max_sub_array_of_size_k1(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k2(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k3(3, [2, 1, 5, 1, 3, 2]))
