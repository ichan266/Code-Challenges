# Leetcode #832
# Flipping an image
# Given an n by n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# * Submission 1
def flipAndInvertImage1(image):
    
    for singleList in image:
        for index in range(len(singleList)):
            if singleList[index] == 1:
                singleList[index] = 0
            else:
                singleList[index] = 1
                
    image = [list[::-1] for list in image]
    
    return image

# * Submission 2
def flipAndInvertImage2(image):

    for singleList in image:
            for index in range(len(singleList)):
                singleList[index] = 1 - singleList[index]
                    
    image = [list[::-1] for list in image]
    
    return image

# * Submission 3
def flipAndInvertImage3(image):

    for singleList in image:
        length  = len(singleList)
        for index in range(int(len(singleList)/2)):
            singleList[index], singleList[length-1-index] = singleList[length-1-index], singleList[index]
        for index in range(len(singleList)):
            singleList[index] = 1 - singleList[index]
                    
    return image

# * Submission 4
def flipAndInvertImage4(image):

    for singleList in image:
        singleList.reverse()
        for index in range(len(singleList)):
            singleList[index] = 1 - singleList[index]
        
        return image

# @ Discussion
# @ 1. (1 - binaryValue) trick:
# @    This is so helpful!!! If I need to convert 0 to 1 OR 1 to 0: 
# @    1 - 0 = 1
# @    1 - 1 = 0
# @    So just need to do this simple math to convert!
# @ 2. Reverse a list: can use several strategies:
# @    a. List' method: .reverse()
# @       This method comes in handy. Can also consider using list[::-1]
# @    b. Divide the list by 2, then leverage on the length and index to do the swap (Submission #3)