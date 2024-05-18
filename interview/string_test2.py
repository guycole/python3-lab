#
# Title: string_test2.py
# Description: character.ai (much better solution)
# there is also a sliding window solution 
# 
# 0942 1007

from typing import Dict

class Solution:

    def execute(self, arg1: str, arg2: str) -> None:
        print("execute")

        target = set(list(arg2))
        # print(target)

        # arg1 permutations
        candidates = []
        for ndx1 in range(len(arg1)):
            for ndx2 in range(ndx1, len(arg1)):
#                print(arg1[ndx1:ndx2+1])
                candidates.append(arg1[ndx1:ndx2+1])

        winner_string = None
        for temp in candidates:
            if len(temp) < len(arg2):
                continue

            intersect = target.intersection(temp)
            # print(f"{temp} {intersect}")
            if len(intersect) == len(arg2):
                if winner_string is None:
                    winner_string = temp
                elif len(temp) < len(winner_string):
                    # print(f"new winner {temp}")
                    winner_string = temp

        return winner_string

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute("CODEBANC", "ABC"))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
