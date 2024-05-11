#
# Title: water_array.py
# Description: 
# 
# 1412 1424

from typing import List


class Solution:
   
   # brute force O(n^2) solution
    def execute1(self, candidates: List[int]) -> int:
        print(f"execute1 {candidates}")

        max_area = -1
        start_ndx = -1
        stop_ndx = -1

        for ndx1 in range(len(candidates)):
            for ndx2 in range(ndx1+1, len(candidates)):
#                print(f"top {ndx1} {candidates[ndx1]} {ndx2} {candidates[ndx2]}")
             
                height = min(candidates[ndx1], candidates[ndx2])
                width = ndx2-ndx1
                area = height * width

                if max_area < area:
                    max_area = area
                    start_ndx = ndx1
                    stop_ndx = ndx2
                    print(f"new max area {max_area} {start_ndx} {stop_ndx}")
                    
        return max_area
    
    # better O(n) solution
    # 1501 1525
    def execute2(self, candidates: List[int]) -> int:
        print(f"execute2 {candidates}")

        max_area = -1
        start_ndx = -1
        stop_ndx = -1

        left_ndx = 0
        right_ndx = len(candidates)-1

        while left_ndx < right_ndx:
            print(f"top {left_ndx} {candidates[left_ndx]} {right_ndx} {candidates[right_ndx]}")

            height = min(candidates[left_ndx], candidates[right_ndx])
            width = right_ndx-left_ndx
            area = height * width

            if area > max_area:
                max_area = area
                start_ndx = left_ndx
                stop_ndx = right_ndx
                print(f"new max area {max_area} {start_ndx} {stop_ndx}")

            if candidates[left_ndx] < candidates[right_ndx]:
                left_ndx = left_ndx + 1
            else:
                right_ndx = right_ndx - 1

        return max_area

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute2([5, 9, 2, 1, 4])) # 16
    print(solution.execute2([5, 9, 2, 4])) # 12
    print(solution.execute2([5, 9, 2, 4, 3, 7])) # 28
    print(solution.execute2([1, 8, 6, 2, 5, 7])) # 28

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
