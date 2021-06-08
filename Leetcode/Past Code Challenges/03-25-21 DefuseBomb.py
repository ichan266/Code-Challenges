# Leetcode #1652
# * Need to refactor to make it run faster
def decrypt(code, k):

    code_length = (len(code))
    result = [0] * code_length

    if k == 0:
        return result

    def wrapCode(idx):
        """Use this function to wrap the list, code. """

        return idx % code_length

    for current in range(code_length):
        if k > 0:
            next = current + 1
            for idx in range(next, next+k):
                result[current] += code[wrapCode(idx)]
        if k < 0:
            next = current + (code_length+k)
            for idx in range(next, next-k):
                result[current] += code[wrapCode(idx)]

    return result
