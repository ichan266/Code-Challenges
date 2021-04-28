# Leetcode 1678
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

class Solution:
    def interpret1(self, command: str) -> str:

        return command.replace("()", "o").replace("(al)", "al")

    def interpret2(self, command: str) -> str:

        result = ""

        for index in range(len(command)):
            if command[index] == "G":
                result += "G"
            elif command[index] == "(":
                if command[index+1] == ")":
                    result += "o"
                elif command[index+1] == "a":
                    result += "al"

        return result
