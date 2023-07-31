#
# Interview question: Given an array of integers, return the indices of the two numbers that add up to a given target
# Solution Type: Optimised solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#
    

def check_integer_list(integer_list, target_value):
    values_required = {}
    list_pointer = 0

    for number in integer_list:  
        
        if number in values_required.keys():
            response = [values_required[number], list_pointer]
            return response
        else:
            number_to_find = target_value - number
            values_required[number_to_find] = list_pointer
            print (values_required)
            
        list_pointer += 1
            

def main():
    user_integer_list = input("Please enter the list of values you'd like within the list: (enter integers separated by a space): ")

    list_of_integers = [int(value) for value in user_integer_list.split()]

    target_value = int(input(f"The chosen list is: {list_of_integers}. What would you like the target to be? (type in an integer value): "))
    print(check_integer_list(integer_list=list_of_integers, target_value=target_value))


main()


