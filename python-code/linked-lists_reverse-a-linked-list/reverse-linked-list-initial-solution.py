#
# Interview question: Given a linked list, reverse it
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#


# Define a node to create a linked list
class Node:
    def __init__(self, value, pointer) -> None:
        self.value = value
        self.pointer = pointer



def reverse_linked_list(head: Node):
    current_node = head
    dictionary = {}
    
    while current_node != None:
        dictionary[len(dictionary)] = current_node.value
        current_node = current_node.pointer
    
    current_node = head
    
    for i in range(0, len(dictionary)):
        current_node.value = dictionary[len(dictionary) - (1+i)]
        current_node = current_node.pointer
    
    return head
        


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







