#
# Title: doormat.py
# Description: create a doormat
#
# 30 minutes

raw_mat = []

def doormat(n, m: int):
    print("doormat")

    for rows in range(n):
        raw_mat.append(["-"]* m)

    pattern = ".|."
    welcome = "WELCOME"

    horizontal_center = m // 2
    vertical_center = n // 2

    offset = len(welcome) // 2
    for ndx1 in range(len(welcome)):
        raw_mat[vertical_center][horizontal_center+ndx1-offset] = welcome[ndx1]

    for rows in range(vertical_center):
        buffer = pattern
        for ndx1 in range(rows):
            buffer = buffer + pattern + pattern

        offset = len(buffer) // 2

        for ndx1 in range(len(buffer)):
            raw_mat[rows][horizontal_center-offset+ndx1]=buffer[ndx1]
            raw_mat[n-1-rows][horizontal_center-offset+ndx1]=buffer[ndx1]

def dumper():
    for rows in range(len(raw_mat)):
      print("".join(raw_mat[rows]))

if __name__ == '__main__':
    print("main")

    doormat(9, 27)
    dumper()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
