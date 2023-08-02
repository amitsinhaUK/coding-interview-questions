#
# Interview question: Given two strings S and T, return if they equal when both are typed out. Any ‘#’ that appears in the string counts as a backspace.
# Solution Type: Initial solution, Time O(a+b), Space O(a+b)
# Code Author: Amit Sinha
#


def final_string(input_string):
    return_string = []
    
    for char in input_string:
        if char == "#" and len(return_string) > 0:
            del return_string[-1]
        elif char != "#":
            return_string.append(char)
    
    return return_string
    
        
def string_match(first_string, second_string):
    final_first_string = final_string(first_string)
    final_second_string = final_string(second_string)
        
    if len(final_first_string) != len(final_second_string):
        return False
    else:
        for pointer in range (0, len(final_first_string)):
            if final_first_string[pointer] != final_second_string[pointer]:
                return False
        return True
    


def main():
    user_first_string = list(input("Please enter the first string: (remember that a '#' represents a backspace): "))
    user_second_string = list(input("Please enter the second string: (remember that a '#' represents a backspace): "))

    print(string_match(first_string=user_first_string, second_string=user_second_string))


main()


