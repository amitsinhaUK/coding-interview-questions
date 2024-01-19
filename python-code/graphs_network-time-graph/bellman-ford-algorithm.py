#
# Interview question: There are n network nodes labelled 1 to N. 
#                     Given a times array, containing edges represented by arrays [u, v, w] where u is the source node, 
#                     v is the target node and w is the time taken to travel from the source node to the target node.
#                     Send a signal from node k, return how long it takes for all nodes to receive the signal. 
#                     Return -1 if it’s impossible.
# Solution Type: Initial solution, Time O(E x log(n) + N x log(n)), Space O(1)
# Code Author: Amit Sinha
#


def bellman_ford_algorithm(edges: list, number_of_nodes: int, start_node:int) -> int:
    min_weight = [float('inf')]*number_of_nodes
    
    min_weight[start_node-1] = 0
    
    for iteration in range (0, number_of_nodes-1):
        for edge in edges:
            source = edge[0]-1
            target = edge[1]-1
            edge_weight = edge[2]
            source_weight = min_weight[source]
            
            if source_weight != float('inf'):
                if (source_weight + edge_weight) < min_weight[target]:
                    min_weight[target] = (source_weight + edge_weight)
    
    return min_weight


# def create_graph(times: list, no_of_nodes: int) -> list:
#     graph = []
    
#     for i in range(0, no_of_nodes):
#         connections = []
        
#         for edge in times:
#             s_node = edge[0] - 1
#             t_node = edge[1] - 1
#             weight = edge[2]
            
#             if s_node == i:
#                 connections.append([t_node, weight])
        
#         graph.append(connections)
    
#     return graph    
    
    
def main():
    s1_times = [[1,2,9], [1,4,2], [2,5,-3], [4,2,-4], [4,5,6], [3,2,3], [5,3,7], [3,1,5]]
    s1_n_value = 5
    s1_k_value = 1
    
    s2_times = [[1, 2, 3], [3, 4, 5]]
    s2_n_value = 4
    s2_k_value = 1
    
    # s1_graph = create_graph(times=s1_times, no_of_nodes=s1_n_value)
    print (f"For S1, the weight is: {bellman_ford_algorithm(edges=s1_times, number_of_nodes=s1_n_value, start_node=s1_k_value)}")

    # s2_graph = create_graph(times=s2_times, no_of_nodes=s2_n_value)
    # print (f"For S2, the graph is: {s2_graph}, the weight is: {dijkstra_algorithm(graph=s2_graph, start_node=s2_k_value-1)}")
    
main()








