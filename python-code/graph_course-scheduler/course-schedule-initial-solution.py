#
# Interview question: There a total of n courses to take, labelled from 0 to n-1. Some courses have prerequisite courses. 
#                     This is expressed as a pair, i.e. [1, 0] which indicates you must take course 0 before taking course 1.
#                     Given the total number of courses and an array of pre-requisite pairs, return if it is possible to finish all the courses.
#
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#

from collections import deque

def breadth_first_search(graph: list) -> bool:
    
    if len(graph) == 0:
        return True
    
    for index in range(0, len(graph)):
        queue = deque()
                
        for pre_req in graph[index]:
            queue.appendleft(pre_req)
            
        while len(queue) > 0:
            current_node = queue.pop()
            
            if current_node == index:
                return False
            
            for pre_req in graph[current_node]:
                queue.appendleft(pre_req)
    
    return True


def build_graph (number_of_nodes: int, pre_reqs: list) -> list:
    graph = []
    
    for i in range (0, number_of_nodes):
        connections = []
        for pre_req in pre_reqs:
            if pre_req[1] == i:
                connections.append(pre_req[0])
                
        graph.append(connections)
    
    return graph


def topological_sort(graph: list) -> bool:
    indegree = [0]*len(graph)

    for edges in graph:     
        if len(edges) > 0:
            for edge in edges:
                indegree[edge] += 1
    
    answer = 0
    
    while (answer < len(graph)) and (0 in indegree):
        index = indegree.index(0)
        
        answer += 1
        for node in graph[index]:
            indegree[node] -= 1
        graph[index] = []
        indegree[index] = -1
        
    if answer == len(graph):
        return True
    else:
        return False
            
                
                
    


def main():
    s1_pre_reqs = [[1,0], [2,1], [2,5], [0,3], [4,3], [3,5], [4,5]]
    s1_n = 6
    s2_pre_reqs = [[4,5], [5,6], [6,4], [0,3], [1,0], [2,1]]
    s2_n = 7
    s3_pre_reqs = []
    s3_n = 0
    
    s1_graph = build_graph(number_of_nodes=s1_n, pre_reqs=s1_pre_reqs)
    s2_graph = build_graph(number_of_nodes=s2_n, pre_reqs=s2_pre_reqs)
    s3_graph = build_graph(number_of_nodes=s3_n, pre_reqs=s3_pre_reqs)
    
    
    # print(f"S1 graph is: {s1_graph}")
    # topological_sort(s1_graph)
    print(f"Graph for s1 is: {s1_graph}. \nCan you take all courses: {topological_sort(s1_graph)}")
    print(f"Graph for s2 is: {s2_graph}. \nCan you take all courses: {topological_sort(s2_graph)}")
    print(f"Graph for s3 is: {s3_graph}. \nCan you take all courses: {topological_sort(s3_graph)}")

     
main()