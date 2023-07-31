#
# Interview question: Given an array of integers, return the indices of the two numbers that add up to a given target
# Solution Type: Initial solution, Time O(n^2), Space O(1)
# Code Author: Amit Sinha
#


def check_for_second_number(integer_list, target_value, list_pointer):
    list_second_pointer = list_pointer + 1

    for pointer in range(list_second_pointer, len(integer_list)):
        if integer_list[pointer] == target_value:
            return pointer
    
    return None
    


def check_integer_list(integer_list, target_value):
    list_pointer = 0

    for number in integer_list:
        number_to_find = target_value - number

        if number_to_find > 0:
            second_pointer = check_for_second_number(integer_list = integer_list, target_value=number_to_find, list_pointer=list_pointer)

            if second_pointer != None:
                response = [list_pointer, second_pointer]
                return response
            
        list_pointer += 1
            


def main():
    user_integer_list = input("Please enter the list of values you'd like within the list: (enter integers separated by a space): ")

    list_of_integers = [int(value) for value in user_integer_list.split()]

    target_value = int(input(f"The chosen list is: {list_of_integers}. What would you like the target to be? (type in an integer value): "))
    print(check_integer_list(integer_list=list_of_integers, target_value=target_value))


main()


