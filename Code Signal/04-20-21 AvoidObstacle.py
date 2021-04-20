def avoidObstacles(inputArray):
    
    maxNum = max(inputArray)
    
    for i in range(2, maxNum):
        found = True
        for num in inputArray:
            if num % i == 0:
                found = False
                break
        if found:
            return i
    
    return maxNum + 1