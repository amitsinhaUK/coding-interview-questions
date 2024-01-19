#
# Interview question: Given a string only containing round brackets ‘(‘ and ‘)’ and lowercase characters, 
#                     remove the lease amount of brackets so the string is valid. A string is valid if it is 
#                     empty or if there are brackets, they all close.
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#

from collections import deque

def bracket_check(input_string: str) -> str:
    string_chars = list(input_string)
    l_stack = deque()
    
    for i in range(0, len(string_chars)):
        char = string_chars[i]
        
        if (char == ")" and len(l_stack) > 0):
            l_stack.pop()
        elif (char == "("):
            l_stack.append(i)
        elif (char ==")" and len(l_stack) == 0):
            string_chars[i]=""
    
    while len(l_stack) > 0:
        position = l_stack.pop()
        string_chars[position] = ""
    
    new_string = "".join(str(char) for char in string_chars)
    return new_string


def main():
    user_string = input("Please enter the string to be used for parentheses check: ")   
    user_string = user_string.lower()
    
    print(bracket_check(input_string=user_string))


main()




