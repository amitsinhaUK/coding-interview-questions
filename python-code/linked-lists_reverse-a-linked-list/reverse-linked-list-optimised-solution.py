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


def reverse_linked_list(head: Node) -> Node:
    previous_node = None
    current_node = head
    next_node = None
    head_pointer = None
    
    while current_node != None:
        next_node = current_node.pointer
        current_node.pointer = previous_node
        previous_node = current_node
        head_pointer = previous_node
        current_node = next_node
        
    return head_pointer


def main ():
    user_string = input("Please enter the value to be reversed: ")
    
    # Create the linked list
    head_node = Node(user_string[0],None)
    previous_value = head_node
    
    for i in range(1, len(user_string)):
        node = Node(user_string[i], None)
        previous_value.pointer = node
        previous_value = node
    
    return reverse_linked_list(head=head_node)
    

main()

