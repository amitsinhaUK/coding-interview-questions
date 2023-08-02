#
# Interview question: Given two strings S and T, return if they equal when both are typed out. Any ‘#’ that appears in the string counts as a backspace.
# Solution Type: Initial solution, Time O(a+b), Space O(1)
# Code Author: Amit Sinha
#


def string_match(first_string, second_string):
    first_str_pointer = len(first_string) -1
    second_str_pointer = len(second_string) -1
    string_match = True
    
    while (first_str_pointer >= 0) and (second_str_pointer >= 0):
        first_str_backspace = 0
        second_str_backspace = 0
        
        print(f"First String Pointer: {first_str_pointer}, Second String Pointer: {second_str_pointer}")
        
        if (first_string[first_str_pointer] == "#"):
            while first_string[first_str_pointer] == "#":
                first_str_backspace += 1
                first_str_pointer -=1
            first_str_pointer -= first_str_backspace
        
        if (second_string[second_str_pointer] == "#"):
            while second_string[second_str_pointer] == "#":
                second_str_backspace += 1
                second_str_pointer -=1
            second_str_pointer -= second_str_backspace
        
        if (first_str_pointer >= 0) and (second_str_pointer >= 0):
            if first_string[first_str_pointer] != second_string[second_str_pointer]:
                string_match = False
                return string_match

            first_str_pointer -= 1
            second_str_pointer -= 1
        
    return string_match
            


def main():
    user_first_string = list(input("Please enter the first string: (remember that a '#' represents a backspace): "))
    user_second_string = list(input("Please enter the second string: (remember that a '#' represents a backspace): "))

    print(string_match(first_string=user_first_string, second_string=user_second_string))


main()

