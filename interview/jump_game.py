#
# Title: jump_gamp.py
# Description: 
# 
#

class Solution:

    def execute(self, candidates: list[int]) -> list[int]:
        print("execute")

        results = []

        current_ndx = 0
        while current_ndx < len(candidates):
            print(f"current {current_ndx} {candidates[current_ndx]}")
            current_ndx = current_ndx + candidates[current_ndx]

            max_jump = -1
            limit = current_ndx+candidates[current_ndx]
            for temp_ndx in range(current_ndx, limit):
                print(f"temp {temp_ndx} {candidates[temp_ndx]} {limit} {candidates[limit]}")
                if max_jump < candidates[temp_ndx]:
                    max_jump = candidates[temp_ndx]

            results.append(max_jump)
            current_ndx = current_ndx + max_jump

        print(f"current {current_ndx}")

#   print(solution.execute([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))


#            max_jump = -1
#            max_jump_ndx = -1

#           
#                if temp_ndx < len(candidates):
#                    print(f"temp {temp_ndx} {candidates[temp_ndx]}")
#
#                    if candidates[temp_ndx] > max_jump:
#                        max_jump = candidates[temp_ndx]
#                        max_jump_ndx = temp_ndx
#
#            current_ndx = current_ndx + max_jump 
#            results.append(max_jump)

#                if temp_ndx + candidates[temp_ndx] >= len(candidates):
#                    results.append(candidates[temp_ndx])
#                    break 

#            if ndx1 + candidates[ndx1] >= len(candidates):
#                results.append(candidates[ndx1])
#                break
#            else:
#                max_jump = 0
#                max_jump_ndx = 0
#                for ndx2 in range(1, candidates[ndx1]+1):
#                    if candidates[ndx1+ndx2] + ndx2 > max_jump:
#                        max_jump = candidates[ndx1+ndx2] + ndx2
#                        max_jump_ndx = ndx2
#
#                results.append(candidates[ndx1+max_jump_ndx])
#                ndx1 = ndx1 + max_jump_ndx

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
