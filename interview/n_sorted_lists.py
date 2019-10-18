#
# Title:n_sorted_lists.py
# Description: sort N sorted lists using heapsort
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Legalise:Copyright (C) 2019 Miserable Bastards, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

from heapq import heappush
from heapq import heappop

#def heapsort1(iterable):
#    h = []
#    for value in iterable:
#        heappush(h, value)
#
#    return [heappop(h) for i in range(len(h))]

def heapsort2(list1, list2):
    candidates = list1

    for ndx in list2:
        heappush(candidates, ndx)

    return [heappop(candidates) for ndx in range(len(candidates))]

if __name__ == '__main__':
    list1 = [3, 5]
    list2 = [1, 5, 12]
    list3 = [6, 6, 6, 11]

    big_list = [list1, list2, list3]
    print(big_list)

    sorted_list = big_list[0]
    for ndx in range(1, len(big_list)):
        sorted_list = heapsort2(sorted_list, big_list[ndx])

    print(sorted_list)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
