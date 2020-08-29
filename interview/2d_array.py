#
# Title:2d_array.py
# Description: 2d array demo
# Development Environment:OS X 10.13.6/Python 3.8.2
# Author:G.S. Cole (guycole at gmail dot com)
#

#  0,  1,  2,  3
#  4,  5,  6
#  7,  8,  9, 10
# 11, 12, 13, 14
candidates = [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14]]

print('start')

#
print(candidates)

# first row
print(candidates[0])

# specific element y, x
print(candidates[2][1])

# print all elements
for row in candidates:
    for column in row:
        print(column, end = " ")
    print()

# insert new row
candidates.insert(2, [4, 3, 2, 1])
print(candidates)

# delete row
del(candidates[1])
print(candidates)

print('stop')

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
