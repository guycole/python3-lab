#
# Title: keypad.py
# Description: discover the time to type a string on a keypad
#

import collections

from typing import List

class Solution:

    def execute(self, input: str, keypad:List[str]) -> int:
        print("execute")

        results = 0

        matmat = collections.defaultdict(tuple)

        # populate matrix with coordinate tuples
        for row in range(len(keypad)):
            for col in range(len(keypad[0])):
                matmat[keypad[row][col]] = (row, col)

        #print(matmat)

        curr_row, curr_col = matmat[input[0]]
        for ndx in range(1, len(input)):
            row, col = matmat[input[ndx]]
            print(f"--> {ndx} {input[ndx]} {matmat[input[ndx]]}")
            distance = abs(row - curr_row) + abs(col - curr_col)
            results += distance
            curr_row, curr_col = matmat[input[ndx]]

        return results

if __name__ == '__main__':
    print("main")

    input = "bfgcil"

    keypad = [
        ["a", "b", "c"],
        ["e", "f", "g"],
        ["h", "i", "l"]
    ]

    solution = Solution()
    print(solution.execute(input, keypad))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
