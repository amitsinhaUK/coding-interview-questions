#
# Interview question: Implement DFS and BFS with a 2D array
# Code Author: Amit Sinha
#

from collections import deque

# Dictionary with the acceptable directions of travel. The key represents the current key and the value is the next direction to try
DIRECTIONS = {
    "up": [-1, 0],
    "right": [0, 1],
    "down": [1,0],
    "left": [0,-1]
}

DIRECTION_ORDER = ["up", "right", "down", "left"]

def _dfs_impl(matrix: list, row: int, column: int, seen: dict, values: list) -> list:
    
    # Base case, at the end of the structure
    max_visits = len(matrix) * len(matrix[0])
    row_max=len(matrix)-1
    column_max=len(matrix[0])-1
    
    if (len(seen) == max_visits) or (not(-1 < row <= row_max)) or (not(-1 < column <= column_max)) or ((row,column) in seen.keys()):
        return values
    
    
    # Record values
    if (row, column) not in seen.keys():
        seen[row, column] = matrix[row][column]
        values.append(matrix[row][column])
    
    row_max=len(matrix)-1
    column_max=len(matrix[0])-1
    
    for direction in DIRECTION_ORDER:
        _dfs_impl(matrix = matrix, row = row + DIRECTIONS[direction][0], column = column + DIRECTIONS[direction][1], seen = seen, values = values)
    
    return values


def depth_first_search(two_d_array: list) -> list:
    positions_visited = {}
    values = []
    
    values = _dfs_impl(matrix=two_d_array, row = 0, column = 0, seen = positions_visited, values = values)
    return values


def _valid_coordinates(row, column, row_max, column_max) -> bool:
    if (-1 < row <= row_max) and (-1 < column <= column_max):
        return True
    else:
        return False

def breadth_first_search(two_d_array:list) -> list:
    queue = deque()
    positions_visited = {}
    values = []
    
    if two_d_array != None and two_d_array[0][0] != None:
        row_index = 0
        column_index = 0
        
        queue.appendleft((row_index, column_index))
        
        while len(queue) > 0:
            coordinates = queue.pop()
            row_index = coordinates[0]
            column_index = coordinates[1]
            
            if (row_index, column_index) not in positions_visited.keys():
                values.append(two_d_array[row_index][column_index])
                positions_visited[(row_index, column_index)] = two_d_array[row_index][column_index]
                        
            for direction in DIRECTION_ORDER:
                row_index = coordinates[0] + DIRECTIONS[direction][0]
                column_index = coordinates[1] + DIRECTIONS[direction][1]
                
                if _valid_coordinates(row = row_index, column = column_index, row_max = len(two_d_array)-1, column_max = len(two_d_array[0]) -1):
                    
                    if (row_index, column_index) not in positions_visited.keys():
                        queue.appendleft((row_index, column_index))

    return values


def main():
    array = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    
    print(depth_first_search(two_d_array=array))
    print(breadth_first_search(two_d_array=array))
    
main()
        