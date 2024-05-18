"""
Problem:

Given an N*M grid of characters, where each cell is either # or *. 
# indicates filled cells in the grid and * indicates empty cells. 
You need to color all empty cells in the grid but you can only use a stamp of size X*Y . 
A stamp can be used to color a X*Y subgrid on this grid only if all the cells in that subgrid are empty. 
You have to tell if all the empty cells of the grid can be colored or not. Output yes or no.

Input
- NxM grid row x col
- Int X rows
- Int Y cols


Example 1:

4*4 grid
3*3 stamp
#***  3 free cells list of free cells
#***
#***
#***

*#** 3 free cells unhelpful because fails 3x3 
#*** 3 free cells ok
#*** 3 free cells ok, and matches previous row
#*** 3 free cells ok and matches preview

 ^.^
***#.  #|#**|
***#.  #|#**|
***#.  #|#**|
***#

Answer: Yes

Example 2:

4*4 grid
3*3 stamp
#***
#***
#***
##** <--- makes it false

#### xxxxxx
####
####
####

Answer: No
"""

# x = row, y = columns
def solution(matrix, x, y):
    results = []

    empty_total = 0

    for row in range(len(matrix)-x):
        for column in range(len(matrix[row]-y)):
            for yy in range(y):
                for xx in range(x):
                    if matrix[yy+row][xx+column] == '*':
                        matrix[yy+row][xx+column] = 'X'
                        empty_total = empty_total + 1

    print(results)

    if empty_total == (x * y):
        return True

    #if empty_total < 

    return False

matrix = []
matrix.append(['#', '*', '*', '*'])
matrix.append(['#', '*', '*', '*'])
matrix.append(['#', '*', '*', '*'])
matrix.append(['#', '*', '*', '*'])

print(solution(matrix, 3, 3))

