#
# Title:intersection.py
# Description: compute the intersection of two lines
# Development Environment:OSX 10.15.7/Python 3.10.7
# Author:G.S. Cole (guycole at gmail dot com)
#
line1 = [[0, 1], [2, 3]]
line2 = [[2, 3], [0, 4]]

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

L1 = line(line1[0], line1[1])
L2 = line(line2[0], line2[1])
R = intersection(L1, L2)
print(R)

line1 = [[0, 0], [3, 3]]
line2 = [[0, 3], [3, 0]]

L1 = line(line1[0], line1[1])
L2 = line(line2[0], line2[1])
R = intersection(L1, L2)
print(R)
