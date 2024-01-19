#
# Interview question: You have a graph of n nodes labeled from 0 to n - 1. 
#                     You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an 
#                     undirected edge between nodes ai and bi in the graph. Return true if the edges of the given graph make up a 
#                     valid tree, and false otherwise.
# Solution Type: Initial solution, Time O(), Space O()
# Code Author: Amit Sinha
#


def union(edges:list, num_nodes: int) -> list:
    root = []
    
    for i in range(0, num_nodes):
        root.append(i)
    
    for edge in edges:
        source = edge[0]-1
        target = edge[1]-1
        
        if root[target] == target:
            root[target] = find(root=root, node=source)
    
    return root


def find(root: list, node: int) -> int:
    if root[node] == node:
        return node
    else:
        return find(root = root, node = root[node])


def create_graph (edges: list, num_nodes: int) -> list:
    graph = [[]]*num_nodes
        
    for i in range(0, num_nodes):
        connections = []
        for edge in edges:
            source = edge[0] - 1
            target = edge[1] - 1
            
            if source == i:
                connections.append(target)
            elif (target) == i:
                connections.append(source)

        graph[i] = connections
        
    return graph
        

def _cycle_in_graph(graph: list, seen: dict, index: int, parent: int) -> bool:
    seen[index] = True
    
    for node in graph[index]:
        
        if node not in seen.keys():
            if _cycle_in_graph(graph=graph, seen=seen, index = node, parent = index):
                return True
            
        elif parent != node:
            return True
    
    return False
    

def is_valid_tree(set: list, graph: list) -> bool:
    root = set[0]
    
    for i in range(0, len(set)):
        if set[i] != root:
            return False
    
    if _cycle_in_graph(graph = graph, seen = {}, index = 0, parent = -1):
        return False
    
    return True
        

def main():
    edges_1 = [[1,2], [2,3], [3,4]]
    edges_1_n = 4
    edges_2 = [[1,2], [2,3], [3,1]]
    edges_2_n = 3
    edges_3 = [[1,2], [3,4]]
    edges_3_n = 4
    
    set_1 = union(edges=edges_1, num_nodes=edges_1_n)
    set_2 = union(edges=edges_2, num_nodes=edges_2_n)
    set_3 = union(edges=edges_3, num_nodes=edges_3_n)
    
    graph_1 = create_graph(edges=edges_1, num_nodes=edges_1_n)
    graph_2 = create_graph(edges=edges_2, num_nodes=edges_2_n)
    graph_3 = create_graph(edges=edges_3, num_nodes=edges_3_n)
    
    print(f"Edges 1 valid binary tree: {is_valid_tree(set=set_1, graph=graph_1)}")
    print(f"Edges 2 valid binary tree: {is_valid_tree(set=set_2, graph=graph_2)}")
    print(f"Edges 3 valid binary tree: {is_valid_tree(set=set_3, graph=graph_3)}")
    
main()

