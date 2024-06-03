#
# Title: mex_array.py
# Description: 
# 
# https://www.geeksforgeeks.org/construct-mex-array-from-the-given-array/
# https://cp-algorithms.com/sequences/mex.html#:~:text=Given%20an%20array%20%24A%24%20of,the%20MEX%20(minimal%20excluded).
# https://codeforces.com/blog/entry/119243#:~:text=Mex%2C%20or%20the%20minimum%20excludant,in%20algorithm%20design%20and%20optimization.
#
# time complexity O(n)

from typing import List


class Solution:

    def execute(self, input: List[int]) -> None:
        print(f"execute {input}")

        MAXN = 11
        flags = [0] * MAXN

        limit = len(input)
        for ndx in range(limit):
            # print(f"{ndx} {input[ndx]}")
            flags[input[ndx]] = 1

        print(f"flags {flags}")

        mexmex = 0
        for ndx1 in range(1, MAXN):
            if flags[ndx1] == 0:
                # missing element
                mexmex = ndx1
                break
    
        print(f"mexmex {mexmex}")

        output = [0] * limit
        for ndx1 in range(limit):
            if input[ndx1] < mexmex:
                output[ndx1] = input[ndx1]
            else:
                output[ndx1] = mexmex

        for ndx1 in range(limit):
            print(f"{output[ndx1]} ", end="")

        print("")

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.execute([2, 1, 5, 3])
    solution.execute([1, 9, 2, 4])
    solution.execute([0, 1, 2, 4, 5])
    solution.execute([0, 1, 2, 3, 4])
    solution.execute([1, 2, 3, 4, 5])

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
