# Code Signal Arcade Intro Problem #56

def digitsProduct(product):

    if product == 1:
        return 10

    if product < 10:
        return product

    smallDigit = []

    test = 9

    while product != 1:
        div, mod = divmod(product, test)
        if mod == 0:
            smallDigit.append(test)
            product = div
        elif mod != 0:
            test -= 1
        if test == 2 and mod != 0:
            return -1

    result = 0

    for digit in smallDigit[::-1]:
        result = (result * 10) + digit

    return result
