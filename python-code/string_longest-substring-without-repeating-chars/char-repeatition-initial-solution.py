#
# Interview question: Given two strings S and T, return if they equal when both are typed out. Any ‘#’ that appears in the string counts as a backspace.
# Solution Type: Initial solution, Time O(n^2), Space O(n)
# Code Author: Amit Sinha
#


def longest_substring(input_string):
    max_size = 0
    
    
    for pointer in range (0, len(input_string)):
        character_map = {}
        trailing_pointer = pointer
        continue_checking = True
        
        character_map[input_string[pointer]] = pointer
        
        if trailing_pointer < len(input_string):    
            while continue_checking:
                character = input_string[trailing_pointer]
                if character not in character_map.keys():
                    character_map[character] = trailing_pointer
                elif (len(character_map) > max_size):
                    max_size = len(character_map)
                    continue_checking = False
                
                trailing_pointer += 1
                
                if trailing_pointer >= len(input_string):
                    if (len(character_map) > max_size):
                        max_size = len(character_map)
                    continue_checking = False
    
    return max_size



def main():
    user_string = list(input("Please enter the string to be checked: "))

    print(longest_substring(input_string=user_string))


main()

