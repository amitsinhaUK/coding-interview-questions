#
# Interview question: Check if there is a cycle within a linked list
# Solution Type: Initial solution, Time O(n), Space O(1)
# Code Author: Amit Sinha
#


# Define a node to create a linked list
class Node:
    def __init__(self, value, pointer) -> None:
        self.value = value
        self.pointer = pointer


def check_for_cycle(head: Node):
    seen_values = {}
    current_node = head
    
    while current_node.pointer != None:
        if current_node.value in seen_values.keys():
            return True
        else:
            seen_values[current_node.value] = current_node
        
        current_node = current_node.pointer
    
    return False
    

def main():
    cycle_list_head = Node("1", None)
    number_list = [2,3,4,5,6]
    
    current_node = None
    previous_node = cycle_list_head
    second_node = None
    
    # Create Cycle list
    for i in number_list:
        current_node = Node(i, None)
        previous_node.pointer = current_node
        
        # Use this to create a cycle between Nodes 2 and 6 
        if i == 2:
            second_node = current_node
        elif i == 6:
            current_node.pointer = second_node
    
        previous_node = current_node
  
    # Create non-cycle list
    non_cycle_list_head = Node("a", None)
    letters_list = ["b", "c", "d"]
    
    current_node = None
    previous_node = non_cycle_list_head
    
    for char in letters_list:
        current_node = Node(char, None)
        previous_node.pointer = current_node
        previous_node = current_node
    
    
    # Check for cycles
    print(f"List with cycle in it returned: {check_for_cycle(cycle_list_head)}")
    print(f"List without cycle in it returned: {check_for_cycle(non_cycle_list_head)}")
        
    
main()


