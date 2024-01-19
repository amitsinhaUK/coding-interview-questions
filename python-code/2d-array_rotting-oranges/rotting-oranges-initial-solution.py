#
# Interview question: Given a 2D array containing 0 (empty cell), 1’s (fresh orange) and 2’s (rotten orange). 
#                     Every minute, all fresh oranges immediately adjacent (all 4 directions – up, down, left and right) to rotten oranges will rot.
#                     How many minutes must pass until all oranges are rotten. 
# Leet code question: https://leetcode.com/problems/rotting-oranges/
# Solution time: T: O(n), S: O(n)
# Code Author: Amit Sinha
#

from collections import deque

DIRECTIONS = [
        [-1, 0],    # UP
        [1, 0],     # DOWN
        [0, -1],    # LEFT
        [0, 1]      # RIGHT
    ]

ROTTEN_ORANGE = 2
FRESH_ORANGE = 1

def _valid_coordinates(row: int, column: int, row_max: int, column_max: int) -> bool:
    if (-1 < row <= row_max) and (-1 < column <= column_max):
        return True
    else:
        return False


def number_of_minutes(array, queue: deque, orange_count: int) -> int:
    minute_count = 0
    row_max = len(array)-1
    column_max = len(array[0])-1
    rotten_orange_queue = queue
    

    
    while (len(queue) > 0) and (orange_count > 0):
        minute_count += 1
        queue_length = len(queue)
        
        while queue_length > 0:
            rotten_orange = rotten_orange_queue.pop()
            queue_length -= 1
            
            for direction in DIRECTIONS:
                row = rotten_orange[0] + direction[0]
                column = rotten_orange[1] + direction [1]
                
                if _valid_coordinates(row=row, column=column, row_max=row_max, column_max=column_max):
                    if array[row][column] == FRESH_ORANGE:
                        orange_count -= 1
                        array[row][column] = ROTTEN_ORANGE
                        queue.appendleft((row,column))
    
    if orange_count > 0: 
        return -1
    else:
        return minute_count
        
                    
def analyse_organges(array) -> int:
    rotting_oranges_queue = deque()
    number_of_oranges = 0
    
    # Base case
    if len(array) < 1:
        return 0
    
    for r in range(0, len(array)):
        for c in range(0, len(array[0])):
            if array[r][c] == FRESH_ORANGE:
                number_of_oranges += 1
            if array[r][c] == ROTTEN_ORANGE:
                rotting_oranges_queue.appendleft((r,c))
    
    return number_of_minutes(array=array, queue=rotting_oranges_queue, orange_count=number_of_oranges)
    

def main():
    one_rotten_orange_array = [
        [2, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1]
    ]
    
    two_rotten_oranges_array = [
        [1, 1, 0, 0, 0],
        [2, 1, 1, 0, 0],
        [0, 0, 1, 1, 2],
        [0, 1, 0, 0, 1]
    ]
    
    empty_array = []
    
    second_empty_array = [
        [],
        []
    ]
    
    print(f"Number of minutes to rot one rotten organge is: {analyse_organges(one_rotten_orange_array)}")
    print(f"Number of minutes to rot two rotten organges is: {analyse_organges(two_rotten_oranges_array)}")
    print(f"Number of minutes to rot empty array is: {analyse_organges(empty_array)}")
    print(f"Number of minutes to rot second empty array is: {analyse_organges(second_empty_array)}")


main()