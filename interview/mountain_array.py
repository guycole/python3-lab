#
# Title: mountain_array.py
# Description: 
# 
# 1117 1126

from typing import List


class Solution:

    def execute(self, candidates: List[int]) -> bool:
        print(f"execute {candidates}")

        if len(candidates) < 3:
            return False
        
        peak_ndx = -1
        peak_value = -1 

        for ndx1 in range(len(candidates)-1):
            if candidates[ndx1] > candidates[ndx1+1]:
                peak_ndx = ndx1
                peak_value = candidates[ndx1]
                break

        print(f"peak noted {peak_ndx} {peak_value}")

        for ndx1 in range(ndx1+1, len(candidates)-1):
            if candidates[ndx1] < candidates[ndx1+1]:
                print(f"fail early at {ndx1}")
                return False

        if peak_ndx < 0:
            return False

        return True

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute([3, 5, 5])) # false
    print(solution.execute([0, 3, 2, 1])) # true
    print(solution.execute([0, 2, 3, 4, 5, 2, 1])) # true

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
