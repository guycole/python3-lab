#
# Title: heap1.py
# Description: heap as an array, not use python libs
# heap is a complete bintree, always balanced 
# heap allows duplicates
#
# https://realpython.com/python-heapq-module/
# https://www.baeldung.com/cs/heap-vs-binary-search-tree

def insert(fresh, candidates):
    print(candidates)

    candidates.append(fresh)
    ii = len(candidates)-1
    print(candidates)

    while candidates[ii//2] > fresh:
        print("%d %d" % (ii, candidates[ii]))
        candidates[ii] = candidates[ii//2-1]
        print(candidates)
        ii = ii//2-1

    candidates[ii] = fresh

    return candidates

print('start')
if __name__ == '__main__':
    print('main')

    candidates = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    candidates = [  13, 21, 16, 24, 31, 19, 68, 65, 26, 32 ]

    result = insert(14, candidates)
    print(result)

    list1 = [3, 5]
    list2 = [1, 5, 12]
    list3 = [6, 6, 6, 11]

    candidates = list1
    print(candidates)
    print(insert(1, candidates))
#    for ndx in list2:
#        candidates = insert(ndx, candidates)

#    for ndx in list3:
#        candidates = insert(ndx, candidates)

#    print(candidates)

#    xx = 14
#    candidates.append(xx)
#    ii = len(candidates)-1

#    while candidates[ii//2] > xx:
#        print(ii)
#        candidates[ii] = candidates[ii//2]
#        ii = ii//2

#    candidates[ii] = xx

#    print(candidates)

print('stop')

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
