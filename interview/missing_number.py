#
# Title: missing_number.py
# Description: discover the missing number
# 
# 1607 1614

from typing import List


class Solution:

    def execute(self, candidates: List[int]) -> int:
        print("execute")

        total = sum(candidates)

        size = len(candidates)
        gauss = size * (size+1)/2

        result = int(gauss) - total

        return result

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute([4, 1, 2, 0]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
