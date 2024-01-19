#
# Interview question: There are n network nodes labelled 1 to N. 
#                     Given a times array, containing edges represented by arrays [u, v, w] where u is the source node, 
#                     v is the target node and w is the time taken to travel from the source node to the target node.
#                     Send a signal from node k, return how long it takes for all nodes to receive the signal. 
#                     Return -1 if it’s impossible.
# Solution Type: Initial solution, Time O(E x log(n) + N x log(n)), Space O(1)
# Code Author: Amit Sinha
#

import heapq

#TO-DO: Implement Heap class and use it instead of inbuilt class
class PriorityQueue():
    def __init__(self, type: str) -> None:
        self.heap = []
        self.heap_type = type
    
    def push(self, value: int):
        pass
    
    def pop(self) -> int:
        pass
    
    def __balance_heap (self):
        pass


def dijkstra_algorithm(graph: list, start_node: int) -> int:
    
    min_heap = []
    heapq.heappush(min_heap, (0, start_node))
    processed = []
    weight = [float('INF')]*len(graph)
    weight[start_node] = 0
    
        
    while (len(min_heap) > 0):
        node_tuple = heapq.heappop(min_heap)
        
        for edge in graph[node_tuple[1]]:
            edge_node = edge[0]
                        
            if edge_node not in processed:
                total_weight = edge[1] + node_tuple[0]
                if total_weight < weight[edge_node]:
                    weight[edge_node] = total_weight
                    heapq.heappush(min_heap, [total_weight,edge_node])
        
        processed.append(node_tuple[1])
        
            
    if len(processed) < len(graph):
        return -1
    else:
        return max(weight)
        
        
def create_graph(times: list, no_of_nodes: int) -> list:
    graph = []
    
    for i in range(0, no_of_nodes):
        connections = []
        
        for edge in times:
            s_node = edge[0] - 1
            t_node = edge[1] - 1
            weight = edge[2]
            
            if s_node == i:
                connections.append([t_node, weight])
        
        graph.append(connections)
    
    return graph    
    
    
def main():
    s1_times = [[1,2,9], [1,4,2], [2,5,1], [4,2,4], [4,5,6], [3,2,3], [5,3,7], [3,1,5]]
    s1_n_value = 5
    s1_k_value = 1
    
    s2_times = [[1, 2, 3], [3, 4, 5]]
    s2_n_value = 4
    s2_k_value = 1
    
    s1_graph = create_graph(times=s1_times, no_of_nodes=s1_n_value)
    print (f"For S1, the graph is: {s1_graph}, the weight is: {dijkstra_algorithm(graph=s1_graph, start_node=s1_k_value-1)}")

    s2_graph = create_graph(times=s2_times, no_of_nodes=s2_n_value)
    print (f"For S2, the graph is: {s2_graph}, the weight is: {dijkstra_algorithm(graph=s2_graph, start_node=s2_k_value-1)}")
    
main()
