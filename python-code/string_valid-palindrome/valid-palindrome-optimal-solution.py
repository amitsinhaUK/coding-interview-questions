#
# Interview question: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring case sensitivity
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#


def palindrome_check(input_string):
    l_pointer = 0
    # You minus 1 because the start is at 0
    r_pointer = len(input_string) -1
    valid_palindrome = True
    
    while (l_pointer <= len(input_string)//2) and (r_pointer >= len(input_string)//2) and valid_palindrome:
        if input_string[l_pointer] != input_string[r_pointer]:
            valid_palindrome = False
        elif input_string[l_pointer] == input_string[r_pointer]:
            valid_palindrome = True
            l_pointer += 1
            r_pointer -= 1
    
    return valid_palindrome



def main():
    user_string = input("Please enter the string for a palindrome check: ")   
    user_string = user_string.lower()
        
    processed_string = ""
    
    for char in user_string:

        if (ord(char) > 96) and (ord(char) < 123):
            processed_string += char        

    print(palindrome_check(input_string=processed_string))


main()



