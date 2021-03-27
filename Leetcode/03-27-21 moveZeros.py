# LeetCode #283
import timeit


def moveZeros(list):

    zero_count = 0
    found_zero = False

    for idx in range(len(list)):
        if list[idx] == 0:
            zero_count += 1
            found_zero = True
        elif list[idx] != 0 and found_zero == True:
            list[idx - zero_count] = list[idx]
            list[idx] = 0

    return list


def moveZeros1(nums):

    n = 0

    for item in nums:
        if item == 0:
            nums.remove(item)
            nums.append(item)
            n += 1
            if len(nums) - n == 0:
                break

    return nums


# Compare the two functions runtime
# The "faster" version: moveZeros
print(timeit.timeit(lambda: moveZeros(
    [0, 1, 0, 3, 12, 0, 0, 1, 4, 6]), number=1000000))

# The "slower" version: moveZeros1
print(timeit.timeit(lambda: moveZeros1(
    [0, 1, 0, 3, 12, 0, 0, 1, 4, 6]), number=1000000))


print(moveZeros([0]))
print(moveZeros([0, 0, 0, 1, 4, 6, 14]))
print(moveZeros([1]))
