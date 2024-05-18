#
# Title: rubrik2.py
# Description: stamping the grid problem
# second version of this problem, this one works
#

from typing import List


class Solution:

    def execute(self, x: int, y: int, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)-y+1):
            for column in range(len(matrix[row])-x+1):
                #print(f"{row} {column}")
                #print(matrix[row][column], end=' ')
                counter = 0
                for yy in range(y):
                    for xx in range(x):
                        #print(matrix[row+yy][column+xx], end=' ')
                        #print(f"{row+yy} {column+xx}")

                        if matrix[row+yy][column+xx] != '#':
                            counter = counter + 1

                if counter == (x * y):
                    # mark all the cells as colored
                    for yy in range(y):
                        for xx in range(x):
                            matrix[row+yy][column+xx] = 'X'

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == '*':
                    return False
               
        return True

if __name__ == '__main__':
    print("main")

    solution = Solution()

    matrix = []
    matrix.append(['#', '*', '*', '*'])
    matrix.append(['#', '*', '*', '*'])
    matrix.append(['#', '*', '*', '*'])
    matrix.append(['#', '*', '*', '*'])
    print(solution.execute(3, 3, matrix))

#    matrix.clear()
#    matrix.append(['a', 'b', 'c', 'd'])
#    matrix.append(['e', 'f', 'g', 'h'])
#    matrix.append(['i', 'j', 'k', 'l'])
#    matrix.append(['m', 'n', 'o', 'p'])

    matrix.clear()
    matrix.append(['#', '*', '*', '*'])
    matrix.append(['#', '*', '*', '*'])
    matrix.append(['#', '*', '*', '*'])
    matrix.append(['#', '#', '*', '*'])
    print(solution.execute(3, 3, matrix))

    matrix.clear()
    matrix.append(['#', '*', '*', '*'])
    matrix.append(['*', '#', '*', '*'])
    matrix.append(['*', '*', '#', '*'])
    matrix.append(['*', '*', '*', '#'])
    print(solution.execute(2, 2, matrix))

    matrix.clear()
    matrix.append(['*', '*', '*', '*'])
    matrix.append(['*', '*', '*', '*'])
    matrix.append(['*', '*', '*', '*'])
    matrix.append(['*', '*', '*', '*'])
    print(solution.execute(3, 3, matrix))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
