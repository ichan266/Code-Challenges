# Code Signal Arcade
def boxBlur(image):

    croppedImageWdth = len(image[0])-2
    croppedImageHt = len(image)-2

    croppedImage = [[0 for y in range(croppedImageWdth)]
                    for x in range(croppedImageHt)]

    for indexRow in range(croppedImageHt):
        for indexColumn in range(croppedImageWdth):
            total = sum(image[indexRow][indexColumn:indexColumn+3]) + sum(image[indexRow+1]
                                                                          [indexColumn:indexColumn+3]) + sum(image[indexRow+2][indexColumn:indexColumn+3])
            croppedImage[indexRow][indexColumn] = total//9

    return croppedImage
