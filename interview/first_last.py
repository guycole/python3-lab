#
# Title: first_last.py
# Description: return the first and last indices of a value in a sorted array
# 1019 1032
#

from typing import List


class Solution:

    # common binary search
    def binary_search(self, target: int, low: int, high: int, candidates: List[int]) -> int:
        if high >= low:
            mid = (high + low) // 2

            if candidates[mid] == target:
                return mid
            elif candidates[mid] > target:
                return self.binary_search(target, low, mid-1, candidates)
            else:
                return self.binary_search(target, mid+1, high, candidates)
        else:
            # target not found
            return -1

    # find first
    def binary_search_low(self, target: int, low: int, high: int, candidates: List[int]) -> int:
        if high >= low:
            mid = (high + low) // 2

            if candidates[mid] == target:
                if candidates[mid-1] == target:
                    return self.binary_search_low(target, low, mid-1, candidates)
                else:
                    return mid
            elif candidates[mid] > target:
                return self.binary_search_low(target, low, mid-1, candidates)
            else:
                return self.binary_search_low(target, mid+1, high, candidates)
        else:
            # target not found
            return -1

    # find last
    def binary_search_high(self, target: int, low: int, high: int, candidates: List[int]) -> int:
        if high >= low:
            mid = (high + low) // 2

            if candidates[mid] == target:
                if candidates[mid+1] == target:
                    return self.binary_search_high(target, mid+1, high, candidates)
                else:
                    return mid
            elif candidates[mid] > target:
                return self.binary_search_high(target, low, mid-1, candidates)
            else:
                return self.binary_search_high(target, mid+1, high, candidates)
        else:
            # target not found
            return -1

    # use binary search
    def execute2(self, target: int, candidates: List[int]) -> List[int]:
        print("execute1")

        result = [-1, -1]

        result[0] = self.binary_search_low(11, 0, len(candidates), candidates)
        result[1] = self.binary_search_high(11, 0, len(candidates), candidates)

        return result

    # brute force
    def execute1(self, target: int, candidates: List[int]) -> List[int]:
        print("execute1")

        result = [-1, -1]
        
        # will throw ValueError if not found
        # temp = candidates.index(target)

        mode_flag = False     
        for ndx1 in range(len(candidates)):
            if mode_flag is True:
                if candidates[ndx1] != target:
                    result[1] = ndx1-1
                    break
            else:
                if candidates[ndx1] == target:
                    result[0] = ndx1
                    mode_flag = True

        return result

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute1(11, [10, 11, 11, 11, 78]))
    print(solution.execute2(11, [10, 11, 11, 11, 78]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
