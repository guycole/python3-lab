#
# Title: move_zero.py
# Description: 
# 
# 1910 1916

from typing import List


class Solution:

    # uses same array
    def execute2(self, candidates: List[int]) -> List[int]:
        print("execute2")

        destination_ndx = 0
        for source_ndx in range(len(candidates)):
            if candidates[source_ndx] > 0:
                candidates[destination_ndx] = candidates[source_ndx]
                destination_ndx = destination_ndx + 1

        for source_ndx in range(destination_ndx, len(candidates)):
            candidates[source_ndx] = 0

        return candidates

    def execute1(self, candidates: List[int]) -> List[int]:
        print("execute1")

        result = [0] * len(candidates)

        destination_ndx = 0
        for source_value in candidates:     
            if source_value > 0:
                result[destination_ndx] = source_value
                destination_ndx = destination_ndx + 1

        return result

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute1([0, 12, 0, 1, 3]))
    print(solution.execute2([0, 12, 0, 1, 3]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
