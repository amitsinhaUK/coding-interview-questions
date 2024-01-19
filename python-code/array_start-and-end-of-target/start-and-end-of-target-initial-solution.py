#
# Interview question: Given an array of integers, return the indices of the two numbers that add up to a given target
# Solution Type: Initial solution, Time O(log(n), Space O(n)
# Code Author: Amit Sinha
#

import math

def binary_search(search_list, search_value):
    
    left_pointer = 0
    right_pointer = len(search_list) -1
    middle_pointer = round(len(search_list) / 2)
       
    while search_list[middle_pointer] != search_value:
        
        if left_pointer == right_pointer and search_list[middle_pointer] != search_value:
            return -1
        if search_list[middle_pointer] < search_value:
            left_pointer = middle_pointer + 1
        elif search_list[middle_pointer] > search_value:
            right_pointer = middle_pointer - 1
        
        
        if left_pointer == right_pointer:
            middle_pointer = right_pointer
        else:
            middle_pointer = round((right_pointer - left_pointer) / 2) + left_pointer
        
    if search_list[middle_pointer] == search_value:
        return middle_pointer
    else:
        return -1



def start_and_end_search(search_list, search_value):
    
    # Set to -100 as -1 upwards has meaning
    
    result=[]
    search_left = False
    search_right = False
    
    if len(search_list) < 1:
        return [-1, -1]
    
    search_index = binary_search(search_list=search_list, search_value=search_value)
    
    print(f"Search index: {search_index}")
    
    # Base Case
    if search_index < 0:
        return [-1, -1]
    
    left_index = -1
    right_index = -1
    
    left_list = search_list[:search_index]
    right_list = search_list[search_index + 1:]

    if len(left_list) > 0:
        search_left = True
    
    if (len(right_list) > 0):
        search_right = True
        
    # Traverse left and right to work out start of values
    while search_left or search_right:
        if search_left:
            left_search = binary_search(left_list, search_value)
            
            print(f"Left Search result: {left_search}, Left List: {left_list}")
            
            if left_search != -1:
                left_index = left_search
                left_list = left_list[:left_search]
                
                if len(left_list) < 1:
                    search_left = False
            else:
                search_left = False
            
        if search_right:
            right_search = binary_search(right_list, search_value)
            
            print(f"Right Search result: {right_search}, Right List: {right_list}")
            
            if right_search != -1:
                right_index = right_search + search_index + 1
                right_list = right_list[right_index + 1:]
                
                if len(right_list) < 1:
                    search_right = False
            else: 
                search_right = False
    
    if left_index < 0:
        result.append(search_index)
    else:
        result.append(left_index)
    
    if right_index < 0:
        result.append(search_index)
    else:
        result.append(right_index)
            
    return result
        


def main():
    user_input = list(input("Please enter the list of values you'd like within the array: (enter integers separated by a space and ensure ordering): ").split())
    user_int_list = [int(x) for x in user_input]
    
    target_value = int(input(f"The chosen array is: {user_int_list}. What would you like the target to be? (type in an integer value): "))
    
    print(f"Binary search result: {start_and_end_search(user_int_list, target_value)}")


main()
