#
# Title: mountain_array.py
# Description: 
# 
# 1117 1126

from typing import List


class Solution:

    def execute(self, candidates: List[int]) -> bool:
        print("execute")

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
            if candidates[ndx1] > candidates[ndx1+1]:
                pass
            else:
                return False

        if peak_ndx < 0:
            return False

        return True

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute([1, 3, 2]))
    print(solution.execute([1, 2, 3, 2, 1]))
    print(solution.execute([1, 2, 3, 2, 1, 4]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
