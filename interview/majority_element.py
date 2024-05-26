#
# Title: majority_elment.py
# Description: 
# 
#

from typing import List


class Solution:

    def execute(self, candidates: List[int]) -> int:
        print("execute")

        majority = len(candidates) // 2
        memento = {}
        results = -1

        for ndx1 in range(len(candidates)):
            if candidates[ndx1] in memento.keys():
                memento[candidates[ndx1]] += 1
            else:
                memento[candidates[ndx1]] = 1

            if memento[candidates[ndx1]] > majority:
                results = candidates[ndx1]
                return results

        return results

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute([2, 1, 3, 1, 1]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
