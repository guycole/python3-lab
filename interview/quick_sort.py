#
# Title: quick_sort.py
# Description: 
# "divide and conquer strategy"
# partition to sub arrays w/a pivot element
# pivot element is crucial to performance
# recursively sort the sub arrays (bad for large array)
# recursion stop when sub array has < 2 elements
# average time complexity O(n log n) 
# worst is O(n^2) when pivot is smallest or largest element
# bad for sorted lists (try insertion sort)
# space complexity O(log n) for recursion worst is O(n)
#


class Solution:

    def swap(self, array:list[int], ii:int, jj:int) -> None:
        array[ii], array[jj] = array[jj], array[ii]

    # pivot is O(n)
    def pivot(self, array:list[int], low_ndx:int, high_ndx:int) -> int:
        swap_ndx = low_ndx

        for ii in range(low_ndx+1, high_ndx+1):
            if array[ii] < array[low_ndx]:
                swap_ndx += 1
                self.swap(array, swap_ndx, ii)

        self.swap(array, low_ndx, swap_ndx)

        return swap_ndx

    # quick_sort is O(n log n)
    def quick_sort(self, array:list[int], low_ndx:int, high_ndx:int) -> None:
        if low_ndx < high_ndx:
            pivot_ndx = self.pivot(array, low_ndx, high_ndx)
            self.quick_sort(array, low_ndx, pivot_ndx-1)
            self.quick_sort(array, pivot_ndx+1, high_ndx)


    def execute(self, array: list[int]) -> list[int]:
        print(f"execute {array}")

        low_ndx = 0
        high_ndx = len(array)-1
 
        self.quick_sort(array, low_ndx, high_ndx)

        return array

if __name__ == '__main__':
    print("main")

    solution = Solution()
    # print(solution.execute([1, 7, 4, 1, 10, 9, -2]))
    print(solution.execute([4, 6, 1, 7, 3, 2, 5]))
    print(solution.execute([4, 6, 1, 7, 3, 2, 9]))

    # print(solution.pivot([4, 6, 1, 7, 3, 2, 5], 0, 6))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
