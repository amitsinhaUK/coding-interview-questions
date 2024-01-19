#
# Interview question: Implement a priority queue as a max heap
# Code Author: Amit Sinha
#

class PriorityQueue:
    import math
    
    def __init__(self) -> None:
        self.tree = []


    def push(self,value: int):
        new_value = value
        self.tree.append(new_value)
        new_value_loc = len(self.tree)-1
        
        parent_loc = self.math.floor((new_value_loc - 1)/2)
        
        if parent_loc > -1 and parent_loc != new_value_loc:
            parent_value = self.tree[parent_loc]

            print(f"New value: {value}, new location: {new_value_loc}, parent value: {parent_value}, parent location: {parent_loc}")
            
            # Whilst the value being added is greater than 
            while parent_value < new_value and parent_loc > -1:
                (self.tree[new_value_loc], self.tree[parent_loc]) = (self.tree[parent_loc], self.tree[new_value_loc])
                
                new_value_loc = parent_loc
                parent_loc = self.math.floor((new_value_loc - 1)/2)
                
                if parent_loc > -1:
                    parent_value = self.tree[parent_loc]
     
     
    def pop(self) -> int:
        value_to_return = self.tree[0]
        
        # Set the last value to the head of the heap and delete from the end
        self.tree[0]=self.tree[len(self.tree) -1]
        del self.tree[len(self.tree)-1]
        
        # Re-position the root of the node correctly
        if len(self.tree) > 1:
            node_loc = 0
            node_value = self.tree[node_loc]
            left_child_loc = (node_loc*2)+1
            right_child_loc = (node_loc*2)+2
            
            max_value = None
            max_loc = None
            
            while (left_child_loc < len(self.tree)):
                left_child_value = None
                right_child_value = None                
                
                if left_child_loc < len(self.tree):
                    left_child_value = self.tree[left_child_loc]
                   
                if right_child_loc < len(self.tree):
                    right_child_value = self.tree[right_child_loc]    
                
                # Find the max value and set the variables to it. Check if the right 
                if left_child_value != None and right_child_value != None:
                    if left_child_value > right_child_value:
                        max_value = left_child_value
                        max_loc = left_child_loc
                    else:
                        max_value = right_child_value
                        max_loc = right_child_loc
                elif left_child_value != None: 
                    max_value = left_child_value
                    max_loc = left_child_loc
                
                if node_value < max_value:
                    (self.tree[node_loc], self.tree[max_loc]) = (self.tree[max_loc], self.tree[node_loc])
                    node_loc = max_loc
                    
                    left_child_loc = (node_loc*2)+1
                    right_child_loc = (node_loc*2)+2
                else:
                    left_child_loc = len(self.tree) + 1
                    right_child_loc = len(self.tree) + 1
                    
        return value_to_return
                
                
    def isEmpty(self) -> bool:
        if len(self.tree) == 0:
            return True
        else:
            return False
    
    def size(self) -> int:
        return len(self.tree)
    
    
    def peek(self):
        return self.tree[0]

    
    def getQ(self) -> list:
        return self.tree


def main():
    priorityQ = PriorityQueue()
    priorityQ.push(50)
    priorityQ.push(45)
    priorityQ.push(25)
    priorityQ.push(40)
    priorityQ.push(35)
    priorityQ.push(10)
    priorityQ.push(15)
    priorityQ.push(20)

    print(f"This is the priority queue: {priorityQ.getQ()}")
    
    priorityQ.push(75)
    
    print(f"This is the priority queue: {priorityQ.getQ()}")
    
    print(f"The max value in the priority queue is: {priorityQ.pop()}")
    print(f"This is the priority queue: {priorityQ.getQ()}")
    
    
main()
