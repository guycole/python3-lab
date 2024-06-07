#
# Title: quick_sort.py
# Description: 
# time complexity O(n logn)
# space complexity O(1)
#


class Solution:
 
    def partition(self, array:list[int], low:int, high:int) -> int:
        pivot = array[high]
        print(f"pivot {pivot} {low} {high}")

        ii = low - 1
        for jj in range(low, high):
            if array[jj] <= pivot:
                ii += 1
                array[ii], array[jj] = array[jj], array[ii]
                print(f"swap ii and jj {ii} {jj} {array}")

        array[ii + 1], array[high] = array[high], array[ii + 1]

        return ii + 1

    def quick_sort(self, candidates:list[int], low:int, high:int) -> None:
        if low < high:
            pivot = self.partition(candidates, low, high)
            self.quick_sort(candidates, low, pivot - 1)
            self.quick_sort(candidates, pivot + 1, high)

    def execute(self, candidates: list[int]) -> list[int]:
        print(f"execute {candidates}")

        low = 0
        high = len(candidates) - 1
 
        self.quick_sort(candidates, low, high)

        return candidates

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute([1, 7, 4, 1, 10, 9, -2]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
