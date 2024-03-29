#
# Title:rangoli.py
# Description: from hacker rank
#

print("start")

if __name__ == "__main__":
    print("main")

    size = 3
    max_char = ord("a") + size - 1
    max_column = 4 * size - 3
    max_row = 2 * size - 1
    center_column = max_column // 2

    population = 1
    row_ndx = 0
    for row in range(max_row):
        buffer = list('-' * max_column)

        char_now = max_char
        for charz in reversed(range(0, population)):
            delta_ndx = charz * 2

            buffer[center_column+delta_ndx] = chr(char_now)
            buffer[center_column-delta_ndx] = chr(char_now)

            char_now -= 1

        print(''.join(buffer))

        row_ndx += 1
        if row_ndx >= size:
            population -= 1
        else:
            population += 1

print("stop")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
