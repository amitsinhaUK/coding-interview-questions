#
# Interview question: Given two strings S and T, return if they equal when both are typed out. Any ‘#’ that appears in the string counts as a backspace.
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#


def longest_substring(input_string):
    
    if len(input_string) == 0:
        return 0
    
    max_size = 1
    start_of_window = 0
    
    char_dictionary = {}
    
    for end_of_window in range(0, len(input_string)):      
        
        current_char = input_string[end_of_window]
        
        if current_char not in char_dictionary.keys():
            char_dictionary[current_char] = end_of_window
                        
        elif (current_char in char_dictionary.keys()):
            
            # Only change window if the value has occured within the window
            if start_of_window <= char_dictionary[current_char]:
                start_of_window = char_dictionary[current_char]+1
            
            # Update the start of the window to the new substring
            char_dictionary[current_char] = end_of_window
        
                    
        # Check and update the max size. Add +1 to account for fact that strings start at 0
        if max_size < (end_of_window - start_of_window + 1):
            max_size = (end_of_window - start_of_window + 1)
    
    return max_size
            
                
def main():
    user_string = list(input("Please enter the string to be checked: "))

    print(longest_substring(input_string=user_string))


main()

