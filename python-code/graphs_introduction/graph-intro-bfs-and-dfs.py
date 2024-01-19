#
# Interview question: Implement breadth first search and depth first search with a graph represented by an adjacency list
# Solution Type: Initial solution, Time O(n), Space O(1)
# Code Author: Amit Sinha
#

from collections import deque

GRAPH = [
    [1, 3], 
    [0],
    [3, 8],
    [0, 4, 5, 2], 
    [3, 6],
    [3],
    [4, 7],
    [6],
    [2]
]


def breadth_first_search(graph:list) -> list:
    queue = deque()
    answer = []
    
    if len(graph) > 0:
        queue.appendleft(0)
    
    while len(queue) > 0:
        index = queue.pop()
        answer.append(index)
        edges = graph[index]
                
        for edge in edges:
            if edge not in answer:
                queue.appendleft(edge)
    
    return answer



def _dfs_impl(graph: list, answers: list, index: int) -> list:
    answers.append(index)
    
    for node in graph[index]:
        if node not in answers:
            _dfs_impl(graph=graph, answers=answers, index=node)
        
    return answers

def depth_first_search(graph:list) -> list:
    return _dfs_impl(graph=graph, answers=[],index=0)

 
def main():
    print(f"Graph BFS Answer: {breadth_first_search(GRAPH)}")
    print(f"Graph DFS Answer: {depth_first_search(GRAPH)}")

main()




