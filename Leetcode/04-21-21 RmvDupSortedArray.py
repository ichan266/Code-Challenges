# Leetcode # 26
def removeDuplicates(nums):
    
    n = 0
    
    while len(nums)-1 > n:
        while len(nums)-1 > n and nums[n] == nums[n+1]:
            nums.pop(n+1)
        n += 1
    
    print(nums)        
    return len(nums)



def removeDuplicates1(nums):

    if not nums:
        return 0

    count = 0

    for num in nums:
        if num != nums[count]:
            count += 1
            nums[count] = num

    print(nums)
    return count + 1

nums = [0,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
nums1 = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates1(nums))