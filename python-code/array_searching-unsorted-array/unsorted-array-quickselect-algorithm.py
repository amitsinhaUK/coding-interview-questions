#
# Interview question: Given an upsorted array, implement quicksort to sort this array
# Solution Type: Initial solution, Time O(n), Space O(1)
# Code Author: Amit Sinha
#

import random 


def partition(input_list, start, end):
    
    partition_index = random.randint(start, end)
    partition_value = input_list[partition_index]
    
    smaller_values_end_index = start
    
    for i in range(start, end):
        if i != partition_index:
            if input_list[i] < partition_value:
                (input_list[i], input_list[smaller_values_end_index]) = (input_list[smaller_values_end_index], input_list[i])
                
                if smaller_values_end_index == partition_index:
                    partition_index = i
                    
                smaller_values_end_index += 1
    
    (input_list[smaller_values_end_index], input_list[partition_index]) = (input_list[partition_index], input_list[smaller_values_end_index])
    return partition_index  


def get_k_value_from_list(input_list, index_req, start_value, end_value) -> int:
       
    index_sorted = partition(input_list=input_list, start=start_value, end=end_value)
    
    if index_req < index_sorted:
        get_k_value_from_list(input_list, index_req, start_value, index_sorted)
    elif index_req > index_sorted:
        get_k_value_from_list(input_list, index_req, index_sorted, end_value)
    
    print(f"Index sorted by partition: {index_sorted}")
    return input_list[index_req]

def main():
    user_input = list(input("Please enter the list of numbers you'd like to be sorted: (remember to keep a space between them): ").split())
    user_value_from_list = int(input("Please the largest value of the list you'd like to return: (type 1 for 1st, 2 for 2nd, 4 for 4th, etc.): "))

    user_number_list = []
    
    for value in user_input:
        user_number_list.append(int(value))
    
    index_required = len(user_number_list) - user_value_from_list
    
    print(get_k_value_from_list(input_list=user_number_list, index_req=index_required, start_value=0, end_value=len(user_number_list)-1))
        

main()


