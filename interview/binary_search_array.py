#
# Title: binary_search_array.py
# Description: 
# 
#

class Solution:

    candidates = []
    result = -1

    def search(self, target: int, left_ndx:int, right_ndx:int, pivot_ndx:int) -> None:
        ref_val = candidates[pivot_ndx]
        print(f"{left_ndx} {right_ndx} {pivot_ndx} {ref_val} {target}")

        if target < ref_val:
            print("less")
            self.search(target, left_ndx, pivot_ndx, pivot_ndx // 2)
        elif target > ref_val:
            print("greater")
            finagle = (right_ndx - pivot_ndx) // 2
            self.search(target, pivot_ndx, right_ndx, pivot_ndx+finagle) 
        else:
            print(f"match {pivot_ndx}")
            self.result = pivot_ndx

    def execute(self, target: int, candidates: list[int]) -> int:
        print("execute")

        self.candidates = candidates
        result = self.search(target, 0, len(candidates)-1, len(candidates)-1)
        return self.result

if __name__ == '__main__':
    print("main")

    candidates = [x for x in range(30)]

    solution = Solution()
    print(solution.execute(13, candidates))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
