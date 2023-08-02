#
# Interview question: Given a doubly linked list, list nodes also have a child property which can point to a separate doubly linked list. 
# These child lists  can also have one or more child doubly linked lists of their own, and so on. 
# Return the list as a single level flattened doubly linked list.
# Leet code link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Solution Type: Initial solution, Time O(n), Space O(1)
# Code Author: Amit Sinha
#


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        head_pointer = head
        current_node = head
                
        while current_node != None:
            if current_node.child != None:
                current_node = self.merge_list(start_node=current_node, end_node=current_node.next, head_list=current_node.child)
            else:
                current_node = current_node.next
        
        return head_pointer
            

    def merge_list(self, start_node, end_node, head_list):
        start_node.next = head_list
        head_list.prev = start_node

        start_node.child = None

        previous_node = None
        node = head_list
                    
        while node != None:
            if node.child != None:
                node = self.merge_list(start_node=node, end_node=node.next, head_list=node.child)

            previous_node = node
            node = node.next
            
        if previous_node != None:
            previous_node.next = end_node
            
        if end_node != None:
            end_node.prev = previous_node
            return end_node
        else:
            return previous_node