#
# Interview question: A company has n employees with unique IDs from 0 to n-1. The head of the company has the ID headID. 
#                     You will receive a managers array where managers[i] is the ID of the manager for employee i. Each employee has one direct manager. 
#                     The company head has no manager (managers[headID] = -1). It’s guaranteed the subordination relationships will have a tree structure.
# 
#                     The head of the company wants to inform all employees of news. He will inform his direct subordinates who will inform their direct subordinates 
#                     and so on until everyone knows the news. 
# 
#                     You will receive an informTime array where informTime[i] is the time it takes for employee I to inform all their direct subordinates. 
#                     Return the total number of minutes it takes to inform all employees of the news. 
#
# Solution Type: Initial solution, Time O(n), Space O(1)
# Code Author: Amit Sinha
#


# def _dfs_impl(graph: list, inform_time: list, mgr_index: int) -> int:
#     max_time = 0
    
#     # Catch base case
#     if graph[mgr_index] != []:
#         directs = graph[mgr_index]
        
#         for direct in directs:
#             additional_time_taken = _dfs_impl(graph=graph, inform_time=inform_time, mgr_index=direct)
            
#             if additional_time_taken > max_time:
#                 max_time = additional_time_taken

        
#     return inform_time[mgr_index] + max_time


def max_inform_time(graph: list, inform_time: list, head_index: int) -> int:
    # return _dfs_impl(graph=graph, inform_time=inform_time, mgr_index=head_index)

    max_time = 0
    
    # Catch base case
    if graph[head_index] != []:
        directs = graph[head_index]
        
        for direct in directs:
            additional_time_taken = max_inform_time(graph=graph, inform_time=inform_time, head_index=direct)
            
            if additional_time_taken > max_time:
                max_time = additional_time_taken

        
    return inform_time[head_index] + max_time


def main():
    best_case_mgr_list = [
    [],
    [],
    [0, 1],
    [],
    [2, 5, 6],
    [7], 
    [3],
    []]
    best_case_inform_time = [0, 0, 4, 0, 7, 3, 6, 0]
    best_case_head_index = 4
    
    one_mgr_list = [ 
    []]
    one_mgr_inform_time = [0]
    one_mgr_head_index = 0
    
    print(f"The max time for the best case is: {max_inform_time(graph=best_case_mgr_list, inform_time=best_case_inform_time, head_index=best_case_head_index)}")
    print(f"The max time for the one manager case is: {max_inform_time(graph=one_mgr_list, inform_time=one_mgr_inform_time, head_index=one_mgr_head_index)}")

    
main()
