#
# Title: kth_largest.py
# Description: 
# 
#

class Solution:
    # sorted in descending order
    results_list = None
    results_max = None
    results_min = None

    def shuffle(self, origin:int, value:int) -> None:
        """ make space in result_list and insert value at origin """
        for ndx in range(len(self.results_list)-2, origin-1, -1):
            print(f"ndx {ndx} {self.results_list[ndx]}")
            self.results_list[ndx+1] = self.results_list[ndx]

        self.results_min = self.results_list[len(self.results_list)-1]

        self.results_list[origin] = value

    def tester(self, candidate) -> None:
        """ discover if candidate fits in results list as kth largest """
        for ndx in range(len(self.results_list)):
            if self.results_list[ndx] is None:       
                self.results_list[ndx] = candidate
                break
            elif candidate > self.results_list[ndx]:
                self.shuffle(ndx, candidate)
                break

    def execute(self, kk: int, candidates: list) -> int:
        print("execute")

        self.results_list = [None] * kk
        self.results_list[0] = candidates[0]
        self.results_max = candidates[0]
        self.results_min = candidates[0]

        for ndx1 in range(1, len(candidates)):
            self.tester(candidates[ndx1])

        return self.results_min

if __name__ == '__main__':
    print("main")

    solution = Solution()
#    solution.results_list = [x for x in range(10)]
#    solution.results_list = solution.results_list[::-1]
#    print(solution.results_list)

#    print("shuffle")
#    solution.shuffle(1, 9)
#    print(solution.results_list)
#    print(solution.results_min)

#    print("tester")
#    solution.tester(5)
#    print(solution.results_list)
#    print(solution.results_min)

    solution.execute(2, [3,2,1,5,6,4])
    print(solution.results_list)
    print(solution.results_min)

    solution.execute(4, [3,2,3,1,2,4,5,5,6])
    print(solution.results_list)
    print(solution.results_min)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
