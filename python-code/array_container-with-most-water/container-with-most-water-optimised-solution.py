#
# Interview question: You are given an array of positive integers where each integer represents the height of a vertical line on a chart.
#                     Find two lines which together with the x-axis forms a container that would hold the greatest amount of water. 
#                     Return the area of water it would hold.
# Solution Type: Optimised solution, Time O(n), Space O(1)
# Code Author: Amit Sinha
#

import array

def calc_max_area(integer_array):
    pointer_head = 0
    pointer_tail = len(integer_array)-1
    
    max_area = 0
    
    while pointer_head < pointer_tail:
        area = min(integer_array[pointer_head], integer_array[pointer_tail]) * (pointer_tail - pointer_head)
        
        if area > max_area:
            max_area = area
            
        if (integer_array[pointer_head] < integer_array[pointer_tail]):
            pointer_head += 1
        else:
            pointer_tail -= 1
        
    return max_area


def main():
    user_integer_list = input("Please enter the list of values you'd like within the list: (enter integers separated by a space): ")

    array_of_integers = array.array('i', (int(value) for value in user_integer_list.split()))

    print(calc_max_area(integer_array=array_of_integers))


main()
