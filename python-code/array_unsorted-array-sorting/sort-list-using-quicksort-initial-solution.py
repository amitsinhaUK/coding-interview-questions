#
# Interview question: Given an upsorted array, implement quicksort to sort this array
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#

import random 

# Space is O(n) for this algorithm
def quicksort(unsorted_list: list):
    
    if len(unsorted_list) < 2:
        return unsorted_list
    
    
    # Pick random number from list length as pivot
    pivot = random.randint(0, len(unsorted_list) - 1)
    pivot_value = unsorted_list[pivot]
    left_side = []
    right_side = []
         
    for i in range (0, len(unsorted_list)):

        if i != pivot:
            # Check if the value in question needs to be 
            if unsorted_list[i] <= pivot_value:
                left_side.append(unsorted_list[i])
            else:
                right_side.append(unsorted_list[i])
    
    return quicksort(left_side)+[pivot_value]+quicksort(right_side)
            

def get_k_value_from_list(sorted_list, k):
    return sorted_list[len(sorted_list)-k]
    

def main():
    user_input = list(input("Please enter the list of numbers you'd like to be sorted: (remember to keep a space between them): ").split())
    user_value_from_list = int(input("Please the largest value of the list you'd like to return: (type 1 for 1st, 2 for 2nd, 4 for 4th, etc.): "))

    user_number_list = []
    
    for value in user_input:
        user_number_list.append(int(value))
    
    sorted_list = quicksort(user_number_list)
    print(f"This is the final list: {user_number_list}")
    print(get_k_value_from_list(sorted_list=sorted_list, k=user_value_from_list))
        

main()

