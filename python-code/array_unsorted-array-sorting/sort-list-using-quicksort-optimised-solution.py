#
# Interview question: Given an upsorted array, implement quicksort to sort this array
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#

import random 

# Space is O(1) for this algorithm
def partition(unsorted_list: list, sort_position_start, sort_position_end):
    
    if len(unsorted_list) < 2:
        0
    
    # Pick random number from list length as pivot
    pivot_index = random.randint(sort_position_start, sort_position_end)
    
    pivot_value = unsorted_list[pivot_index]
    print(f"Pivot index is: {pivot_index}, pivot value is: {pivot_value}")
    
    # Set a variable to find the final resting place. Ensure (to begin with) that it is outside the bounds of the list before we get going
    no_of_smaller_values = sort_position_start
    
    # Iterate through the list with 2 pointers - a no_of_smaller_values pointer for the right position in the list of the pivot 
    # and a pointer j to traverse the list
    for j in range(sort_position_start, sort_position_end + 1):
        
        print(f"Current value of j: {j}, current value of no_of_smaller_values: {no_of_smaller_values}, Pivot value: {pivot_value}, Unsorted list: {unsorted_list}")
        
        # Check if the value at j is the same as the pivot point (and if so, skip over it)
        if j != pivot_index:
            
            # Check if the value of j is less than or equal to the pivot value. The reason to do this is that we want everything to the left of the pivot
            # value to be less than the pivot value itself. no_of_smaller_values will only increment if the value is less than or equal the number (it's effectively
            # a count on the number of values which are smaller or equal to the pivot value itself)
            
            if unsorted_list[j] <= pivot_value:
                
                # Catch for the pivot value changing because the number of small items is greater than the index of the pivot value
                # The pivot value in this case becomes the value of j, given the swap
                if no_of_smaller_values == pivot_index:
                    pivot_index = j
                
                # Swap the values for j and no_of_smaller_values so that the higher value is to the right of the pointer
                print(f"Swapping values: {unsorted_list[no_of_smaller_values]}, {unsorted_list[j]}")
                (unsorted_list[no_of_smaller_values], unsorted_list[j]) = (unsorted_list[j], unsorted_list[no_of_smaller_values])
                
                # Increment the final resting place by 1 as you've found a value in the list which goes to the left of the pivot
                no_of_smaller_values += 1
    
    
    if pivot_index != no_of_smaller_values:
        # Swap location of value at pivot point to it's final_resting_place
        print(f"Final swap before return: {unsorted_list[pivot_index]} and {unsorted_list[no_of_smaller_values]}. Current list: {unsorted_list}")
        (unsorted_list[pivot_index], unsorted_list[no_of_smaller_values]) = (unsorted_list[no_of_smaller_values], unsorted_list[pivot_index])
    
    print(f"Final value of no_of_smaller_values: {no_of_smaller_values}, Pivot value: {pivot_value}, Final list before return: {unsorted_list}\n\n")
    return no_of_smaller_values
    
    
def quicksort(unsorted_list: list, start, end):
    
    # Base Case catch 
    if start < end:
        
        # Create partition
        list_partition = partition(unsorted_list=unsorted_list, sort_position_start=start, sort_position_end=end)
        
        if list_partition > start:
            quicksort (unsorted_list, start, list_partition-1)
        
        if list_partition < end:
            quicksort (unsorted_list, list_partition+1, end)
            

def get_k_value_from_list(sorted_list, k):
    return sorted_list[len(sorted_list)-k]
    

def main():
    user_input = list(input("Please enter the list of numbers you'd like to be sorted: (remember to keep a space between them): ").split())
    user_value_from_list = int(input("Please the largest value of the list you'd like to return: (type 1 for 1st, 2 for 2nd, 4 for 4th, etc.): "))

    user_number_list = []
    
    for value in user_input:
        user_number_list.append(int(value))
    
    quicksort(unsorted_list=user_number_list, start = 0, end = len(user_number_list)-1)
    print(f"Partition of list: {user_number_list}. List is: {user_number_list}")
    print(get_k_value_from_list(sorted_list=user_number_list, k=user_value_from_list))
        

main()

