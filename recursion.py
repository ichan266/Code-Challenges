def factorialRecur(num):
    """ Taken in an integer and return result of its factorial product using recursion."""

    # Base Case
    if num == 1:
        return 1

    # recursion in the return statement with num-1 as its argument
    return num * factorialRecur(num-1)


def factorialIter(num):
    """ Taken in an integer and return result of its factorial product using iteration."""

    total = 1

    for i in range(1, num+1):
        total *= i

    return total


num = 5
print(f"Recursion: num = {num}, result = {factorialRecur(num)}")
print(f"Iteration: num = {num}, result = {factorialIter(num)}")


# % from Al Sweigart's youtube video: https://youtu.be/AfBqVVKg4GE
# % Using iteration to emulate recursion

callStack = []  # holding the "frame objects"
# "Call" the factorial() function
callStack.append({"instrPtr": "start", "number": 7})
returnValue = None

while len(callStack) > 0:
    # The body of the "factorial() function":

    number = callStack[-1]["number"]  # Set number "parameter"
    instrPtr = callStack[-1]["instrPtr"]

    if instrPtr == "start":
        if number == 1:
            # * Base Case
            returnValue = 1
            callStack.pop()  # "return" from "function all"
            continue
        else:
            # * Recursive Case
            callStack[-1]["instrPtr"] = "after recursive call"
            # "Call" the "factorial() function":
            callStack.append({"instrPtr": "start", "number": number-1})
            continue
    elif instrPtr == "after recursive call":
        returnValue *= number
        callStack.pop()  # "return from function call"

# print(returnValue)

# @ Tail Call Optimization/Elimination (TCO)
# @ In code, tail call optimization/elimination is when the recursive function call is the last thing in the function before it returns:
# @      def recursiveFunc(params):
# @          # blah blah blah
# @             return recursiveFunc(params)
# @
# @ You won't need to hold on to local variables, because there's no code after the recursive call that will need them
# @
# @ There is no need to keep the frame object on the call stack
# @
# @ TCO prevents stack overflow since you can go beyond 1000 function calls
# @
# @ Example:


def factorial(number, accumulator=1):  # will only run up to number=997
    if number == 0:
        # BASE CASE
        return accumulator
    else:
        # RECURSIVE CASE
        return factorial(number-1, number*accumulator)


# print(factorial(997))
