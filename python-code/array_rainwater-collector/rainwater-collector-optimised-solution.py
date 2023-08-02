#
# Interview question: Given an array of integers representing an elevation map where the width of each bar is 1, return how much rainwater can be trapped. 
# Solution Type: Initial solution, Time O(n), Space O(1)
# Code Author: Amit Sinha
#

import array

def calc_area (integer_array):
    total_water = 0
    
    max_l = 0
    max_r = 0
    
    # Initialise the left and right pointers
    pointer_l = 0
    pointer_r = len(integer_array)-1
    
    max_l = 0
    max_r = 0
    
    while pointer_l < pointer_r:        
        if (integer_array[pointer_l] <= integer_array[pointer_r]):
            if integer_array[pointer_l] < max_l:
                total_water += min(max_l, integer_array[pointer_r]) - integer_array[pointer_l]
            else:
                max_l = integer_array[pointer_l]
            
            pointer_l += 1
                
        elif (integer_array[pointer_l] > integer_array[pointer_r]):
            if integer_array[pointer_r] < max_r:
                total_water += min(integer_array[pointer_l], max_r) - integer_array[pointer_r]
            else:
                max_r = integer_array[pointer_r]
            
            pointer_r -= 1
   
        
    return total_water
            

def main():
    user_integer_list = input("Please enter the list of values you'd like within the array: (enter integers separated by a space): ")

    array_of_integers = array.array('i', (int(value) for value in user_integer_list.split()))

    print(calc_area(integer_array=array_of_integers))


main()


