#
# Title: jump_gamp.py
# Description: 
# 
#

class Solution:

    def execute(self, candidates: list[int]) -> list[int]:
        print("execute")

        results = []

        ndx1 = 0
        while ndx1 < len(candidates):
            print(f"current {ndx1} {candidates[ndx1]}")
            if ndx1 + candidates[ndx1] >= len(candidates):
                results.append(candidates[ndx1])
                break
            else:
                max_jump = 0
                max_jump_ndx = 0
                for ndx2 in range(1, candidates[ndx1]+1):
                    if candidates[ndx1+ndx2] + ndx2 > max_jump:
                        max_jump = candidates[ndx1+ndx2] + ndx2
                        max_jump_ndx = ndx2

                results.append(candidates[ndx1+max_jump_ndx])
                ndx1 = ndx1 + max_jump_ndx

        return results

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))

#1, 3, 9, 9

#1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
#10



#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
