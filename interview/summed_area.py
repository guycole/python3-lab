#
# Title: summed_area.py
# Description: summed area table
# https://medium.com/@anubhavroh/integral-image-141f6181db5e
# https://stackoverflow.com/questions/2277749/calculate-the-sum-of-elements-in-a-matrix-efficiently
# https://www.geeksforgeeks.org/submatrix-sum-queries/
#
# space complexity is O(m*n)
# time complexity for range sum query is O(1)
# time complexity for updating value is O(m*n)
#

class Solution:

    def calculate_summed_area_table(self, matmat: list[int]) -> list[int]:

        # calculate summed area table
        sat = [[0 for _ in range(len(matmat[0]))] for _ in range(len(matmat))]

        # calculate first row
        sum = 0
        for ndx in range(len(matmat)):
            sum += matmat[0][ndx]
            sat[0][ndx] = sum

        # calculate first column
        sum = 0
        for ndx in range(len(matmat)):
            sum += matmat[ndx][0]
            sat[ndx][0] = sum

        # calculate sub matrices
        for sat_row in range(1, len(matmat)):
            for sat_col in range(1, len(matmat[0])):
                #print(f"{sat_row} {sat_col}")

                sum = 0
                for row in range(sat_row+1):
                    for col in range(sat_col+1):
                        #print(f"sub matrix {row} {col}")
                        sum += matmat[row][col]

                sat[sat_row][sat_col] = sum

        # print(sat)

        return sat

    def execute(self, target: list, matmat: list[int]) -> int:
        print("execute")

        sat = self.calculate_summed_area_table(matmat)
        print(sat)

        results = 0

        # top left
        row_a = target[0][0] -1
        col_a = target[0][1] -1
        print(f"row_a: {row_a} col_a: {col_a} sat: {sat[row_a][col_a]}") 

        # top right
        row_b = row_a
        col_b = target[1][1] 
        print(f"row_b: {row_b} col_b: {col_b} sat: {sat[row_b][col_b]}") 

        # bottom left
        row_c = target[1][0] 
        col_c = col_a 
        print(f"row_c: {row_c} col_c: {col_c} sat: {sat[row_c][col_c]}") 

        # bottom right
        row_d = row_c 
        col_d = target[1][1]
        print(f"row_d: {row_d} col_d: {col_d} sat: {sat[row_d][col_d]}") 

        results = sat[row_d][col_d] - sat[row_b][col_b] - sat[row_c][col_c] + sat[row_a][col_a]

        return results

if __name__ == '__main__':
    print("main")

    matmat1 = [
        [0, 1, 4],
        [2, 3, 2],
        [1, 2, 7]
    ]

    target1 = [(1, 1), (2, 2)]

    matmat2 = [
        [ 4, 5, 2, 1],
        [ 0, 9, 3, 2],
        [ 5, 6, 8, 1],
        [ 2, 3, 0, 0]
    ]

    target2 = [(1, 1), (2, 3)]

    solution = Solution()
    print(solution.execute(target1, matmat1)) # 14
    print(solution.execute(target2, matmat2)) # 29

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
