#
# Title: dna_rotation.py
# Description: return unique DNA sequence
#

from typing import List

class Solution:

    def execute(self, candidates: List[str]) -> int:
        print("execute")

        database = {}

        for candidate in candidates:
            temp = sorted(candidate)
            database["".join(temp)] = 1

        return len(database)

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute(["TGAAA", "ATGAA", "AATGA"]))
    print(solution.execute(["AAA", "TAA", "TAT", "ATA"]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
