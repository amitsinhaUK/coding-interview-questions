#
# Interview question: Given a 2D array containing only 1’s (land) and 0’s (water), count the number of islands. An island is land connected horizontally or vertically. 
# Leet code question: https://leetcode.com/problems/number-of-islands/
# Solution time: T: O(n), S: O(n)
# Code Author: Amit Sinha
#

from collections import deque


def _island_check(array, row, column, values_seen) -> dict:
    
    DIRECTIONS = [
        [-1 , 0],    # UP
        [0, 1],      # RIGHT
        [1, 0],      # DOWN
        [0, -1]      # LEFT
    ]
    
    row_max = len(array) - 1
    column_max = len(array[0]) -1    
    queue = deque()
    queue.appendleft((row, column))
    
    while len(queue) > 0:
        coordinates = queue.pop()
        coordinate_row = coordinates[0]
        coordinate_column = coordinates[1]
        
        # print(f"while loop - row: {coordinate_row}, column: {coordinate_column}")
        
        if array[coordinate_row][coordinate_column] == 1:
            for direction in DIRECTIONS:
                r = coordinates[0] + direction[0]
                c = coordinates[1] + direction[1]
                
                if (-1 < r <= row_max) and (-1 < c <= column_max):
                    # print(f"Direction is: {direction}, row: {r}, column: {c}")
                    value = array[r][c]
                    
                    if value == 1 and ((r,c) not in values_seen.keys()):
                        queue.appendleft((r,c))
                        values_seen[r,c] = value
                        
    return values_seen
              
              
def number_of_islands(array) -> int:
       
    if len(array) == 0:
        return 0
    
    islands = 0

    values_seen = {}

    for r in range(0, len(array)):
        for c in range (0, len(array[r])):
            
            # print(f"row value: {r}, column value: {c}, island count: {islands}, values seen: {values_seen}")
            
            if (r,c) not in values_seen.keys():
                if (array[r][c] == 1):
                    islands += 1
                    values_seen = _island_check(array = array, row = r, column = c, values_seen = values_seen)
                # else:
                #     values_seen[r,c] = array[r][c]
    
    return islands
    

def main():
    two_island_array = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1]
    ]
    
    seven_island_array = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1]
    ]
    
    empty_array = []
    
    second_empty_array = [
        [],
        []
    ]
    
    print(f"Number of islands on two_island_array is: {number_of_islands(two_island_array)}")
    print(f"Number of islands on seven_island_array is: {number_of_islands(seven_island_array)}")
    print(f"Number of islands on empty_array is: {number_of_islands(empty_array)}")
    print(f"Number of islands on second_empty_array is: {number_of_islands(second_empty_array)}")



main()