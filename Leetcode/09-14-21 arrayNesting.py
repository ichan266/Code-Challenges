# Leetcode # 565
# Array Nesting
# Medium
# https://leetcode.com/problems/array-nesting/

def arrayNesting(nums: list[int]) -> int:

    result = 0
    seen = set()

    for i in range(len(nums)):
        start = nums[i]
        count = 0
        while True:
            if start not in seen:
                count += 1
                seen.add(start)
                start = nums[start]
            else:
                result = max(result, count)
                break

    return result
