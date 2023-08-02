#
# Interview question: Given a linked list, reverse it
# Solution Type: Initial solution, Time O(n), Space O(1)
# Code Author: Amit Sinha
#


# Define a node to create a linked list
class Node:
    def __init__(self, value, pointer) -> None:
        self.value = value
        self.pointer = pointer


def reverse_linked_list(head: Node, start, end) -> Node:
    head_pointer = head
    iterator = 1
    previous_value = None
    current_value = None
    next_value = None
    
    search_stopped = None
    start_reversal = None
    
    # Deals with scenario where reversal starts at beginning of list
    if start == 1:
        start_reversal = head
    else:
        head_pointer = head
        search_stopped = head
        # start - 1 is node before the start of the reversal. This is key for post transformation, otherwise beginnning of the list will be lost
        while iterator < start - 1:
            search_stopped = search_stopped.pointer
            iterator += 1
    
        # Node where reversal starts is stored seperately for the final pointer
        start_reversal = search_stopped.pointer 
        
        # Add 1 to iterator as start of reveral node found
        iterator += 1
    
    current_value = start_reversal
    
    while (start <= iterator) and (iterator <= end):
        next_value = current_value.pointer
        current_value.pointer = previous_value
        previous_value = current_value
        current_value = next_value
        iterator += 1
    
    # Catches scenario where start of list is reversed
    if search_stopped != None:
        search_stopped.pointer = previous_value
    
    start_reversal.pointer = current_value
        
    if next_value == None and start == 1:
        head_pointer = previous_value
    elif start == 1:
        while next_value != None:
            head_pointer = next_value
            next_value = next_value.pointer
    
    return head_pointer
    
    

def main ():
    user_string = input("Please enter the value to be reversed: ")
    start_value = int(input("Enter the start value for the linked list reversal: (enter an integer number): "))
    end_value = int(input("Enter the end value for the linked list reversal: (enter an integer number): "))
    
    # Create the linked list
    head_node = Node(user_string[0],None)
    previous_value = head_node
    
    for i in range(1, len(user_string)):
        node = Node(user_string[i], None)
        previous_value.pointer = node
        previous_value = node
    
    check = reverse_linked_list(head=head_node, start = start_value, end = end_value)
    
    while check != None:
        print(f"Current value {check.value}")
        check = check.pointer
           
main()
