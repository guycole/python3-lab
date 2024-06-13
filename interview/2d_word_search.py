#
# Title: 2d_word_search.py
# Description: 
# 
# 1550

from typing import List

class Solution:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def solution(self, board, word, x, y, cur):
        if(x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] == ' '):
            return False
        cur += board[x][y]

        if(len(cur) > len(word)):
            return False
        if(cur[len(cur)-1] != word[len(cur)-1]):
            return False
        if(cur == word):
            return True

        temp = board[x][y]
        board[x][y] = ' '

        for i in range(4):
            if(self.solution(board, word, x+self.dx[i], y+self.dy[i], cur)):
                return True

        board[x][y] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if(len(word) == 0):
            return True
        
        n = len(board)
        for i in range(n):
            m = len(board[i])
            for j in range(m):
                if(word[0] == board[i][j] and self.solution(board, word, i, j, "")):
                    return True
                
        return False

    def distance(self, loc1: tuple, loc2:tuple) -> bool:
        row_diff = loc1[0] - loc2[0]
        col_diff = loc1[1] - loc2[1]

        print(f"{loc1} {loc2} {row_diff} {col_diff}")

        if row_diff == 0 and col_diff == 0:
            # origin
            return False

        if abs(row_diff) == 1 and abs(col_diff) == 1:
            # diagonal
            return False

        if abs(row_diff) > 1 or abs(col_diff) > 1:
            return False

        print("adjacent")
        return True

    def execute(self, target: str, matmat: list[list[int]]) -> bool:
        print("execute")
        #print(matmat)

        buffer = []
        target_ndx = 0

        candidates = {}

        # build dictionary of character locations
        for row in range(len(matmat)):
            for col in range(len(matmat[0])):
                loc_tuple = (row, col)

                temp = matmat[row][col]
                if temp in candidates:
                    candidates[temp].append(loc_tuple)
                else:
                    candidates[temp] = [loc_tuple]

        current_loc = None
        current_ndx = 0

        for current_ndx in range(len(target)-1):
            print(f"top {current_ndx} {target[current_ndx]}")

            if target[current_ndx] in candidates:
                cur_loc = candidates[target[current_ndx]]
            else:
                # can never succeed
                print("missing current {target[current_ndx]}")
                return False

            next_ndx = current_ndx+1
            if target[next_ndx] in candidates:
                next_loc = candidates[target[next_ndx]]
            else:
                # can never succeed
                print("missing next {target[next_ndx]}")
                return False

            # are they adjacent
            for ndx1 in range(len(cur_loc)):
                for ndx2 in range(len(next_loc)):
                    self.distance(cur_loc[ndx1], next_loc[ndx2])

        return False

    def execute3(self, target: str, matmat: list[list[int]]) -> bool:
        buffer = []
        target_ndx = 0

        current_loc = None
        current_ndx = 0

        for current_ndx in range(len(target)-1):
            next_ndx = current_ndx+1
            print(f"current {target[current_ndx]} next {target[next_ndx]}")

            for row in range(len(matmat)):
                for col in range(len(matmat[0])):
                    temp = matmat[row][col]
                    if temp == target[current_ndx]:
                        print(f"hit {row} {col}")


if __name__ == '__main__':
    print("main")

    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    solution = Solution()
#    solution.execute('ABCCED', board1)
#    solution.execute('SEE', board1)
    print(solution.exist(board1, 'SEE'))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
