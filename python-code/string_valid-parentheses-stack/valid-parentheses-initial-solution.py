#
# Interview question: Given a string containing only parentheses, determine if it is valid. The string is valid if all parentheses close
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#

from collections import deque


def check_parentheses (input_string):
    stack = deque()
    
    for char in input_string:
        if (char == "{") or (char == "[") or (char == "("):
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            
            last_bracket = stack.pop()
            
            if (last_bracket == "{" and  char != "}") or (last_bracket == "[" and  char != "]") or (last_bracket == "(" and  char != ")"):
                return False
    
    # Check if there are any non-closed parentheses        
    if len(stack) > 0:
        return False
    else:
        return True


def main():
    user_string = input("What string would you like to check?: ")
    
    print(check_parentheses(user_string))

main()
