#
# Title: merge1.py
# Description: merge two sorted lists

def merge(list1, list2):
    print("merge")

    result = []

    limit1 = len(list1)
    limit2 = len(list2)

    ndx1 = 0
    ndx2 = 0

    while True:
        if ndx1 == limit1:
            # list1 is exhausted
            if ndx2 == limit2:
                # list2 is exhausted
                return result
            else:
                # list2 is not exhausted
                result.append(list2[ndx2])
                ndx2 += 1
        else:
            # list1 is not exhausted
            if ndx2 == limit2:
                # list2 is exhausted
                result.append(list1[ndx1])
                ndx1 += 1
            else:
                # list2 is not exhausted
                if list1[ndx1] < list2[ndx2]:
                    result.append(list1[ndx1])
                    ndx1 += 1
                else:
                    result.append(list2[ndx2])
                    ndx2 += 1

    return None

print('start')
if __name__ == '__main__':
    print('main')

    list1 = [1, 2, 4]
    list2 = [1, 3, 4, 5]

    result = merge(list1, list2)
    print(result)

print('stop')

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
