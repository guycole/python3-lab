#
# Title: word_search.py
# Description: 
# 
#

class Solution:
    dx = [ 0, 0, -1, 1]
    dy = [-1, 1,  0, 0]

    saved_candidates = []

    matmat = None

    def dumper(self) -> None:
        for row in range(len(self.matmat)):
            for col in range(len(self.matmat[row])):
                print(self.matmat[row][col], end=' ')
            print()

    def is_legal(self, candidate: tuple[int, int]) -> bool:
        row = candidate[0]
        col = candidate[1]

        if row < 0 or row >= len(self.matmat):
            return False

        if col < 0 or col >= len(self.matmat[row]):
            return False
        
        if self.matmat[row][col] == ' ':
            return False

        return True

    def saver(self, candidate: tuple[int, int, str]) -> None:
        self.saved_candidates.append(candidate)
        self.matmat[candidate[0]][candidate[1]] = ' '

    def tester(self, origin: tuple[int, int], candidates: str, candidate_ndx: int) -> bool:
        self.saver((origin[0], origin[1], target[0]))

        if candidate_ndx == len(target):
            print("win win win")
            return True

        for ndx in range(1, len(target)):
            for ndx2 in range(len(self.dx)):
                row = origin[0] + self.dx[ndx2]
                col = origin[1] + self.dy[ndx2]

                location = (row, col)
                if self.is_legal(location):
                    if self.matmat[row][col] == target[candidate_ndx]:
                        print(f"found {target[candidate_ndx]} at {row} {col}")
                        if self.tester(location, target, candidate_ndx + 1) is True:
                            return True

        return False

    def execute(self, target: str, matmat: list[list[str]]) -> bool:
        print("execute")

        self.matmat = matmat
      
        candidates = list(target)

        # discover the first letter
        for row in range(len(matmat)):
            for col in range(len(matmat[row])):
                if candidates[0] == matmat[row][col]:
                    print(f"found {candidates[0]} at {row} {col}")
                    result = self.tester((row, col), candidates, 1)
                    print(f"back with {result}")

        return False

if __name__ == '__main__':
    print("main")

    matmat = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    target = 'SEE'

    solution = Solution()
    print(solution.execute(target, matmat))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
