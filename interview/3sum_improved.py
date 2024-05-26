#
# Title: 3sum_improved.py
# Description: discover a triplet which matches the target sum
#

from typing import List


class Solution:

    def execute(self, target:int, candidates:List[int]) -> List[int]:
        print("execute")

        memento = {}
        results = [-1, -1, -1]

        for ndx1 in range(len(candidates)):
            memento[candidates[ndx1]] = ndx1

        for ndx1 in range(len(candidates)):
            for ndx2 in range(ndx1+1, len(candidates)):
                print(f"{ndx1} {ndx2}")
                delta = target - candidates[ndx1] - candidates[ndx2]
                if delta in memento.keys():
                    results[0] = ndx1
                    results[1] = ndx2
                    results[2] = memento[delta]
                    return results

        print(memento)

        return results

if __name__ == '__main__':
    print("main")

    solution = Solution()
    results = solution.execute(24, [12, 3, 4, 1, 6, 9])
    print(results)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
