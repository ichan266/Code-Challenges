# Leetcode #9
def isPalindrome(num):

    str_num = str(num)

    mid = len(str_num)//2

    back_index = -1
    for index in range(mid):
        if str_num[index] != str_num[back_index]:
            return False
        back_index -= 1

    return True
