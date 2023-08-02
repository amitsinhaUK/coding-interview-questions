#
# Interview question: You are given an array of positive integers where each integer represents the height of a vertical line on a chart.
#                     Find two lines which together with the x-axis forms a container that would hold the greatest amount of water. 
#                     Return the area of water it would hold.
# Solution Type: Initial solution, Time O(n^2), Space O(1)
# Code Author: Amit Sinha
#

import array

def calc_max_area (integer_array):
    max_area = 0
    head_pointer = 0
    
    for value in integer_array:
        for index in range(head_pointer, len(integer_array)):
            height = min(value, integer_array[index])
            width = index - head_pointer
            area = height * width
            
            if area > max_area:
                max_area = area
        head_pointer += 1
    
    return max_area

 

def main():
    user_integer_list = input("Please enter the list of values you'd like within the list: (enter integers separated by a space): ")

    array_of_integers = array.array('i',([int(value) for value in user_integer_list.split()]))

    print(calc_max_area(integer_array=array_of_integers))


main()


