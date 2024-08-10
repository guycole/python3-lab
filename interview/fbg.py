# Overview:
# Write a program, in any language, that will display an ASCII chart given the following data
# data = {(1,2), (2, 3), (3, 1), (4, 6), (5, 8)}.
# You should be able to print the surrounding components of the chart and then place an * where 
# each data point is specified in the data set. You do not need to print the X and Y legends 
# but that would be helpful. You are given the max x and max y but if you can calculate that 
# it would be helpful.
# 
#  Online auction graph display
#  x axis is time
#  y axis is price
#  Title item
#  Given a two-dimension array graph the price over time
# 
#     +-----+-----+-----+-----+-----+-----+
#     +                             *     +
#     +                                   +
#     +                       *           +
#   $ +                                   +
#     +                                   +
#     +           *                       +
#     +     *                             +
#     +                 *                 +
#     +-----+-----+-----+-----+-----+-----+
#                time 
# 
#   max x = 5
#   max y = 8
#   data = {(1,2), (2, 3), (3, 1), (4, 6), (5, 8)}
#
# (x, y)

from re import X

max_x = 5
max_y = 8
data = {(1,2), (2, 3), (3, 1), (4, 6), (5, 8)}
tick_val = 5 # dashes to int

def banner():
    buffer = ['-'] * ((max_x+1) * tick_val) 
    for ndx in range(0, len(buffer), tick_val):
        buffer[ndx] = '+'

    buffer.append('+')

    print(''.join(buffer))

def write_line(buffer:list) -> None:
    buffer[0] = '+'
    buffer[-1] = '+'

    print(''.join(buffer))

def solution():
    # row as key, columns as value
    dd = {}
    for ndx in data:
        row = ndx[1]
        col = ndx[0]

        if row in dd:
            dd[row].append(col)
        else:
            dd[row] = [col]

    banner()

    for ndx in range(max_y, 0, -1):
        buffer = [' '] * ((max_x+1) * tick_val + 1)

        temp = dd.get(ndx)
        if temp is not None:
            for ndx2 in temp:
                buffer[(ndx2*(tick_val))] = '*'

        write_line(buffer)    

    banner()

solution()
