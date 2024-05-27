#
# Title: 4sum.py
# Description: discover a quadruplet which matches the target sum
#

from typing import List


class Solution:

    def execute(self, a:List[int], b:List[int], c:List[int], d:List[int]) -> int:
        print("execute")

        memento = {}
        result = 0
        
        for ndx1 in a:
            for ndx2 in b:
                total = ndx1 + ndx2

                if total not in memento.keys():
                    memento[total] = 1
                else:
                    memento[total] += 1

        for ndx1 in c:
            for ndx2 in d:
                total = -(ndx1 + ndx2)

                if total in memento.keys():
                    result += memento[total]

        print(memento)

        return result

if __name__ == '__main__':
    print("main")

    a = [1, 2]
    b = [-2, -1]
    c = [-1, 2]
    d = [0, 2]

    solution = Solution()
    print(solution.execute(a, b, c, d))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
