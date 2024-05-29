#
# Title: permute1.py
# Description: how many permutations
#

def recurser(original, answer, current, index):
    # print(current)
    if (index > len(original)):
        return

    answer.append(current[:])

    for ndx in range(index, len(original)):
        if (original[ndx] not in current):
            current.append(original[ndx])
            recurser(original, answer, current, ndx)
            current.pop()
            
    return

def solver(original):
    answer = []
    current = []
    recurser(original, answer, current, 0)

    return answer

print('start')
if __name__ == '__main__':
    print('main')

    original = ['a', 'b', 'c']

    results = solver(original)
    print(len(results))
    print(results)
    
print('stop')

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
