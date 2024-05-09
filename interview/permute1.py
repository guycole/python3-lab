#
# Title: permute1.py
# Description: how many permutations
#

print('start')
if __name__ == '__main__':
    print('main')

    original = ['a', 'b', 'c', 'd']

    candidates = []
    for ndx1 in range(len(original)):
        for ndx2 in range(ndx1+1, len(original)):
            candidates.append(original[ndx1:ndx2+1])

    print(len(candidates))
    print(candidates)
    
print('stop')

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***