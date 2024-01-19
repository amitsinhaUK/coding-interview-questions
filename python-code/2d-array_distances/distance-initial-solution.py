#
# Interview question: Given a 2d array containing -1’s (walls), 0’s (gates) and INF’s (empty room). Fill each empty room with the number of steps to the nearest gate. 
#                     If it is impossible to reach a gate, leave INF as the value. INF is equal to 2147483647.
# Solution time: T: O(n), S: O(n)
# Code Author: Amit Sinha
#

from collections import deque


# CONST value declarations

DIRECTIONS = [
    [-1, 0],    # UP
    [1, 0],     # DOWN
    [0, -1],    # LEFT
    [0, 1]      # RIGHT
]
GATE = 0
WALL = -1


def _is_valid_coordinates(row, column, row_max, column_max) -> bool:
    if (-1 < row <= row_max) and (-1 < column <= column_max):
        return True
    else:
        return False


def bfs_map_values(array, queue) -> list:
    
    row_max = len(array)-1
    column_max = len(array[0])-1
    
    while len(queue) > 0:
        coordinates = queue.pop()
        
        distance = array[coordinates[0]][coordinates[1]]
        
        for direction in DIRECTIONS:
            r = coordinates[0] + direction[0]
            c = coordinates[1] + direction[1]
    
            if _is_valid_coordinates(row = r, column = c, row_max = row_max, column_max = column_max):
                if (array[r][c] == float('inf')) or (array[r][c] > distance + 1):
                    array[r][c] = distance + 1
                    queue.appendleft((r,c))
    
    return array
        



def dfs_map_values(array, coordinates, current_step, row_max, column_max):
    
    for direction in DIRECTIONS:
        row = coordinates[0] + direction[0]
        column = coordinates[1] + direction[1]
        
        if _is_valid_coordinates(row = row, column= column, row_max=row_max, column_max=column_max):
            if (array[row][column] != -1) and (array[row][column] > current_step):
                array[row][column] = current_step
                
                dfs_map_values(array=array,coordinates=(row,column), current_step=current_step+1,row_max=row_max, column_max=column_max)
    
    return array
    


def bfs_map_array(array) -> list:
    queue = deque()
    
    # Base case
    if len(array) < 1:
        return []
    
    for r in range(0, len(array)):
        for c in range (0, len(array[0])):
            if array[r][c] == GATE:
                queue.appendleft((r,c))
        
    return bfs_map_values(array, queue)


def dfs_map_array(array) -> list:

    # Base case
    if len(array) < 1:
        return []
    
    row_max = len(array) -1
    column_max = len(array[0]) -1
    
    for r in range(0, len(array)):
        for c in range (0, len(array[0])):
            if array[r][c] == GATE:
                dfs_map_values(array=array, coordinates=(r,c), current_step=1, row_max=row_max, column_max=column_max)
        
    return array




def main():
    
    inf = float('inf')
    
    all_values_accessible_array = [
        [inf, -1, 0, inf],
        [inf, inf, inf, inf],
        [inf, -1, inf, -1],
        [0, -1, inf, inf]
    ]
    
    
    one_inf_left_array = [
        [inf, -1, 0, inf],
        [inf, inf, inf, inf],
        [inf, -1, inf, -1],
        [0, -1, -1, inf]
    ]
    
    empty_array = []
    
    second_empty_array = [
        [],
        []
    ]
    
    print(f"final array for all values accessible is: {dfs_map_array(all_values_accessible_array)}")
    print(f"final array for one value inaccessible is: {dfs_map_array(one_inf_left_array)}")
    print(f"final array for empty array 1 is: {dfs_map_array(empty_array)}")
    print(f"final array for empty array 2 is: {dfs_map_array(second_empty_array)}")

main()
