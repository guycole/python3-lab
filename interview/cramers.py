#
# Title:cramers.py
# Description: solve a system using cramers rule
# Development Environment:OSX 10.15.7/Python 3.10.7
# Author:G.S. Cole (guycole at gmail dot com)
#

# x + y = 5
# 2x - 3y = -4

# (1,  1,  5)
# (2, -3, -4)

a = [[1, 1], [2, -3]]
b = [[5], [-4]]

d = a[0][0] * a[1][1] - a[1][0] * a[0][1]

dx = b[0][0] * a[1][1] - b[1][0] * a[0][1]

dy = a[0][0] * b[1][0] - a[1][0] * b[0][0]

x = dx/d
y = dy/d

print(f"solution:{x},{y}")