#
# Interview question: Given a binary tree, imagine you’re standing to the right of the tree. 
#                     Return an array of the values of the nodes you can see ordered from top to bottom
# Solution: Time: O(n), Space: O(n)
# Code Author: Amit Sinha
#

from collections import deque

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
                
def rhs_breadth_first_search(binary_tree: BinaryTree) -> list:    
    parent_queue = deque()
    parent_queue.appendleft(binary_tree.root_node)
    answer = []
    
    while len(parent_queue) > 0:
        
        child_nodes_queue = deque()
        rhs_value_captured = False
        
        while len(parent_queue) > 0:
            node = parent_queue.pop()
            
            if node != None:
                if rhs_value_captured == False:
                    answer.append(node.value)
                    rhs_value_captured = True
                
                if node.right != None:
                    child_nodes_queue.appendleft(node.right)
                    
                if node.left != None: 
                    child_nodes_queue.appendleft(node.left)

        parent_queue = child_nodes_queue
    
    return answer


def rhs_depth_first_search(node: Node, answer: list, depth_counter: int) -> list:
    if node != None:
        
        if len(answer) < depth_counter:
            answer.append(node.value)
        
        depth_counter += 1
        
        if node.right != None:
            rhs_depth_first_search(node.right, answer, depth_counter)
        
        if node.left != None:
            rhs_depth_first_search(node.left, answer, depth_counter)
    
    return answer


def main():
    binary_tree = BinaryTree(Node(100, None, None))
    
    binary_tree.insert(100)
    binary_tree.insert(50)
    binary_tree.insert(150)
    binary_tree.insert(25)
    binary_tree.insert(75)
    binary_tree.insert(40)
    binary_tree.insert(60)
    binary_tree.insert(30)
    binary_tree.insert(125)
    binary_tree.insert(130)
    binary_tree.insert(175)
    
    # binary_tree = BinaryTree(None)
    
    print(f"RHS of Binary tree with BFS is: {rhs_breadth_first_search(binary_tree=binary_tree)}")
    
    print(f"RHS of Binary tree with DFS is: {rhs_depth_first_search(binary_tree.root_node, answer=[], depth_counter=1)}")


main()