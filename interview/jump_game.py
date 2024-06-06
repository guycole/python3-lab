#
# Title: jump_game.py
# Description: 
# 
#

class Solution:

    # returns true if end can be reached
    # leet code medium 
    # simply iterate through the list and keep track of the maximum jump
    def execute2(self, candidates: list[int]) -> bool:     
        value = 0
        for ndx in candidates:
            if value < 0:
                return False
            elif ndx > value:
                value = ndx
            value -= 1

        return True

    # this version picks the maximum jump from the current index
    # can pick any value to jump from the current index
    # from geeks for geeks, not really trust
    def execute1(self, candidates: list[int]) -> int:
        print(f"execute {len(candidates)} {candidates}")

        results = []

        current_ndx = 0
        while current_ndx < len(candidates):
            max_jump = 0

            limit = min(current_ndx+candidates[current_ndx], len(candidates)-1)
            print(f"top with current:{current_ndx} {candidates[current_ndx]} limit:{limit}")

            for temp_ndx in range(current_ndx+1, limit+1):
                # print(f"temp {temp_ndx} {candidates[temp_ndx]} {limit} {candidates[limit]}")
                if max_jump < candidates[temp_ndx]:
                    #print(f"new max_jump {candidates[temp_ndx]}")
                    max_jump = candidates[temp_ndx]

            max_jump = candidates[current_ndx]

            results.append(max_jump)
            current_ndx = current_ndx + max_jump

            print(f"bottom with next_ndx:{current_ndx} {results}")

        return len(results)

if __name__ == '__main__':
    print("main")

    solution = Solution()
#    print(solution.execute1([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])) #1, 3, 9, 9
#    print(solution.execute1([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

    print(solution.execute2([2, 3, 1, 1, 4]))
    print(solution.execute2([3, 2, 1, 0, 4]))
    print(solution.execute2([0]))
    print(solution.execute2([2, 0, 0]))
    print(solution.execute2([2, 5, 0, 0]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
