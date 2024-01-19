#
# Interview question: Given a binary tree, determine if it is a valid binary search tree.
# Solution: Time: O(n), Space: O(n)
# Code Author: Amit Sinha
#

from collections import deque
import math

class Node:    
    def __init__(self, value: int, left_pointer, right_pointer) -> None:
        self.value = value
        self.left = left_pointer
        self.right = right_pointer
    
    
class BinaryTree:
    def __init__(self, root_node: Node) -> None:
        self.root_node = root_node
    
    def find_position(self, value: int) -> dict:
        search = True
        current_node = self.root_node
        parent_node = None
        node_placement = {}
        
        while search:
            if current_node.value == value:
                return {}
            elif current_node.value < value:
                if current_node.right != None:
                    parent_node = current_node
                    current_node = current_node.right
                    search = True
                else:
                    node_placement["target"] = current_node
                    node_placement["parent"] = parent_node
                    search = False
            elif current_node.value > value:
                if current_node.left != None:
                    parent_node = current_node
                    current_node = current_node.left
                    search = True
                else:
                    node_placement["target"] = current_node
                    node_placement["parent"] = parent_node
                    search = False
        
        return node_placement
    
    def insert(self, value: int):
        tree_info = self.find_position(value)
        additional_node = Node(value, None, None)
        
        if len(tree_info) > 0:
            value_parent_node = tree_info["target"]
            
            if value_parent_node.value > value:
                value_parent_node.left = additional_node
            else:
                value_parent_node.right = additional_node
        else:
            return None
        
        return additional_node
    
    
    def delete (self, value) -> bool:
        tree_info = self.find_position(value)

        if len(tree_info) > 0:
            target_node = tree_info["target"]
            parent_node = tree_info["parent"]
            
            if target_node.left == None and target_node.right == None:
                if target_node.value > parent_node.value:
                    parent_node.right = None
                    return True
                elif target_node.value < parent_node.value:
                    parent_node.left = None
                    return True
            elif target_node.left == None and target_node.right != None:
                if target_node.value > parent_node.value:
                    parent_node.right = target_node.right
                    return True
                elif target_node.value < parent_node.value:
                    parent_node.left = target_node.right
                    return True
            elif target_node.left != None and target_node.right == None:
                if target_node.value > parent_node.value:
                    parent_node.right = target_node.left
                    return True
                elif target_node.value < parent_node.value:
                    parent_node.left = target_node.left
                    return True
            elif target_node.left != None and target_node.right != None:
                
                target_l_node = target_node.left
                target_l_node_value = target_l_node.value
                target_r_node = target_node.right
                
                current_node = target_r_node
                previous_node = None
                
                left_node_placed = False
                
                while not left_node_placed:
                    if target_l_node_value < current_node.value:
                        if current_node.left == None:
                            current_node.left = target_l_node
                            left_node_placed = True
                        elif current_node.left != None:
                            previous_node = current_node
                            current_node = current_node.left
                    elif target_l_node_value > current_node.value:
                        if current_node.right == None:
                            current_node.right = target_l_node
                            left_node_placed = True
                        elif current_node.right != None:
                            previous_node = current_node
                            current_node = current_node.right
                
                if target_node.value > parent_node.value:
                    parent_node.right = target_node.left
                    return True
                elif target_node.value < parent_node.value:
                    parent_node.left = target_node.left
                    return True

# Less than value is the value in which the node has to be less than (i.e. node.value < 5)
# Greater than value is the value in which the node has to be greater than (i.e. node.value > 5)
def valid_tree(node: Node, less_than_value: int, greater_than_value: int) -> bool:
    valid = True
    
    if node != None:
        if node.value >= less_than_value:
            return False
    
    if node != None:
        if node.value <= greater_than_value: 
            return False
    
    if node.left != None:
        valid = valid_tree(node=node.left, less_than_value=node.value, greater_than_value=greater_than_value)
    
    if valid != False and node.right != None:
        valid = valid_tree(node=node.right, less_than_value=less_than_value, greater_than_value=node.value)
        
    return valid
         
                
def main():
    binary_tree = BinaryTree(Node(9, None, None))
    binary_tree.insert(5)
    binary_tree.insert(15)
    binary_tree.insert(1)
    binary_tree.insert(7)
    binary_tree.insert(11)
    binary_tree.insert(19)
    
    # binary_tree = BinaryTree(None)  
        
    print(f"Binary Search tree verdict: {valid_tree(node=binary_tree.root_node, less_than_value=float('inf'), greater_than_value=float('-inf'))}")
        
    
main()
    