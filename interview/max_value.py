#
# Title:max_value.py
# Description: find the max value of consecutive integers
#

if __name__ == '__main__':
    print('main')

    list1 = [-2, 11, -4, 13, -5, -2]

    ranger = [ii for ii in range(len(list1))]
    print(ranger)

    maxx = -999
    for ndx1 in ranger:
        for ndx2 in ranger[1+ndx1:]:
            temp = sum(list1[ndx1:ndx2+1])
            if temp > maxx:
                print(f"new max {temp}")
                maxx = temp

#    for count, item in enumerate(list1):
#        print(f"{count} {item}")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
