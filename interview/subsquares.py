#
# Title: subsquares.py
# Description: given a large square, test if array of smaller squares can be cut
#
# 0 | 0 | 0
# 0 | 0 | 0
# 0 | 0 | 0
#
raw_square = []

def matcher(candidate):
    print(f"matcher: {candidate}")

    for ii in range(len(raw_square)):
        for jj in range(len(raw_square[0])):
            print(f"ii:{ii} jj:{jj} candidate:{candidate}")
            if ii + candidate > len(raw_square):
                print("degenerate1")
                continue
            if jj + candidate > len(raw_square[0]):
                print("degenerate2")
                continue

            if raw_square[ii][jj] == 0:
                for ndx1 in range(candidate-1):
                     for ndx2 in range(candidate-1):
                        print(f"ndx1:{ndx1} ndx2:{ndx2}")
                         if raw_square[ii+ndx1][jj+ndx2] != 0:
                            print("degenerate3")
                            continue

                # winner
                print(f"winner {ii} {jj}")
                raw_square[ii][jj] = 1
                for ndx1 in range(candidate):
                    for ndx2 in range(candidate):
                        print(f"assign {ii+ndx1} {jj+ndx2}")
                        raw_square[ii+ndx1][jj+ndx2] = 1

                return True

    return False

def dumper():
    for ii in range(len(raw_square)):
        for jj in range(len(raw_square[0])):    
            print(raw_square[ii][jj], end=" ")
        print()


def square(m, n, s):
    """ flat piece m x n cut into squares of size s"""
    print("squares")

    raw_square.clear()
    for ndx in range(m):
        raw_square.append([0] * n)

    print(raw_square)

    for ndx in s:
        if matcher(ndx):
            print("matched")
        else:
            return False
    
    return True

if __name__ == '__main__':
    print("main")

    print(square(4, 4, [1, 1, 2]))
    print(raw_square)
    dumper()

    print(square(4, 4, [2, 2]))
    print(raw_square)
    dumper()

    print(square(4, 4, [2, 2, 2]))
    print(raw_square)
    dumper()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
