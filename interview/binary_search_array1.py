#
# Title: binary_search1.py
# Description: 
# binary search requires sorted array 
# runtime O(log n)

class Solution:

    def execute(self, target: int, array: list[int]) -> int:
        left = 0
        right = len(array) - 1
        middle = len(array) // 2
        results = -1
        flag = True

        while flag is True:
            print(f"left: {left}, right: {right}, middle: {middle}")

            if target == array[middle]:
                results = middle
                flag = False
            elif target < array[middle]:
                right = middle - 1
            else:
                left = middle + 1

            middle = (left + right) // 2

            if left > right:
                flag = False    

        return results

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute(12, [10, 11, 12, 13, 14, 15]))
    print(solution.execute(5, [10, 11, 12, 13, 14, 15]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
