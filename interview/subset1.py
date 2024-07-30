#
# Title: subset1.py
# Description: how many subsets
#

def recurser(original, answer, current, index):
#    print(current)
    if index > len(original):
        print("max1")
        return

    #answer.append(current[:])
    answer.append(current.copy())
    #print(answer)

    for ndx in range(index, len(original)):
        #print(f"{index} {len(original)}")
        if original[ndx] in current:
            pass
            #print(f"skipping {ndx} {original[ndx]}")
        else:
            current.append(original[ndx])
        #    print(f"-->{original[ndx]} {current}")
            recurser(original, answer, current, ndx)
            xx = current.pop()
            print(f"popped {xx} {current}")
            
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
