#
# Interview question: Given an array of integers representing an elevation map where the width of each bar is 1, return how much rainwater can be trapped. 
# Solution Type: Initial solution, Time O(n^2), Space O(1)
# Code Author: Amit Sinha
#

import array


def calculate_max_l(integer_array, pointer):
    max_value = 0
    for index in range(0, pointer): 
        if integer_array[index] > max_value:
            max_value = integer_array[index]
    return max_value


def calculate_max_r(integer_array, pointer):
    max_value = 0
    for index in range(pointer + 1, len(integer_array)): 
        if integer_array[index] > max_value:
            max_value = integer_array[index]
    return max_value


def calc_area (integer_array):
    total_water = 0
    max_l = 0
    max_r = 0
    
    for index in range(0, len(integer_array)):
        if index > 0:
            max_l = calculate_max_l(integer_array=integer_array, pointer=index)
            max_r = calculate_max_r(integer_array=integer_array, pointer=index)
        
        if (min(max_l, max_r) - integer_array[index])>0:
            total_water += min(max_l, max_r) - integer_array[index]
    
    return total_water
            

def main():
    user_integer_list = input("Please enter the list of values you'd like within the array: (enter integers separated by a space): ")

    array_of_integers = array.array('i', (int(value) for value in user_integer_list.split()))

    print(calc_area(integer_array=array_of_integers))


main()

