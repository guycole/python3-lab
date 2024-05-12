#
# Title: boat_rescue.py
# Description: 
# 
#

from typing import List


class Solution:
    # O(n log n)
    def execute(self, limit: int, candidates: List[int]) -> int:
        print("execute")

        candidates2 = sorted(candidates)
        result = 0

        left_ndx = 0
        right_ndx = len(candidates) - 1

#        print(f"{candidates[left_ndx]}, {candidates[right_ndx]}")

        while right_ndx >= left_ndx:
            if candidates2[left_ndx] + candidates2[right_ndx] >= limit:
                result = result+1
                right_ndx = right_ndx-1
            else:
                result = result+1
                left_ndx = left_ndx+1
                right_ndx = right_ndx-1

        return result

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute(4, [1, 2, 3, 3]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
