# Coderbyte
# Brute Force
# def FindIntersection(strArr):
    # To house the result:
    # result = []

    # create 2 lists:
        # separate them by using *.split(', )
    # list1 = [int(num) for num in strArr[0].split(', ')]
    # list2 = [int(num) for num in strArr[1].split(', ')]

    # loop through one of them and compare to see if it is in the other list
    # If it is, convert that value to result
    
    # return ",".join(result)

def FindIntersection(strArr):
    # list1 = set(map( int, strArr[0].split(',')))
    # list2 = set(map( int, strArr[1].split(',')))

    list1 = set([int(num) for num in strArr[0].split(', ')])
    list2 = set([int(num) for num in strArr[1].split(', ')])
    # ans = sorted(list(list1 & list2))
    # val = list(map(str, ans))
    # ans = [str(num) for num in sorted(list(list1 & list2))]
    # return ",".join([str(num) for num in sorted(list(list1 & list2))])
    return ",".join([str(num) for num in sorted(list(list1 & list2))])
    


strArr = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]

print(FindIntersection(strArr))