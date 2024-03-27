#
# Title: 3sum.py
# Description: discover a triplet which matches the target sum
#

if __name__ == '__main__':
    print("main")

    input = [12, 3, 4, 1, 6, 9]
    sum = 24

    for ndx1 in range(len(input)):
        for ndx2 in range(ndx1+1, len(input)):
            for ndx3 in range(ndx2+1, len(input)):
                total = input[ndx1]+input[ndx2]+input[ndx3]
                if total == sum:
                    print("found: ", input[ndx1], input[ndx2], input[ndx3])
                    break

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
