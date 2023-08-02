#
# Interview question: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring case sensitivity
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#

def almost_palindrome_check(input_string):
    # Create a left and a right pointer. The left pointer starts at the beginning of the string and the right pointer starts at the end.
    # The characters at each pointer will be compared. If they match, continue checking, if they don't match, work out if by discarding 1 position
    # they will match. If they do, then move the pointer one position but set the char_removed flag to True. Continue checking until non-match scenario
    # is encountered or the check is complete and return the flag almost_palindrome 
    l_pointer = 0
    r_pointer = len(input_string) -1
    char_removed = False
    almost_palindrome = True
    
    while (l_pointer <= r_pointer) and almost_palindrome:
        if input_string[l_pointer] != input_string[r_pointer]:
            if char_removed:
                almost_palindrome = False
            else:
                if (input_string[l_pointer +1] == input_string[r_pointer]):
                    l_pointer += 1
                    char_removed = True
                elif (input_string[l_pointer] == input_string[r_pointer-1]):
                    r_pointer -= 1
                    char_removed = True
                else:
                    almost_palindrome = False
                
        elif input_string[l_pointer] == input_string[r_pointer]:
            almost_palindrome = True
            l_pointer += 1
            r_pointer -= 1
    
    return almost_palindrome



def main():
    user_string = input("Please enter the string for a palindrome check: ")   
    user_string = user_string.lower()
        
    processed_string = ""
    
    for char in user_string:

        if (ord(char) > 96) and (ord(char) < 123):
            processed_string += char        

    print(almost_palindrome_check(input_string=processed_string))


main()


