# binary tree example
#
#
#
class Solution:

    # tree = [None] * 10
    tree = []

    def get_node(self, ndx: int) -> int:
        return self.tree[ndx]

    def execute(self, candidates: list[int]) -> int:
        for ndx1 in candidates:
            self.tree.append(ndx1)

        print(self.tree)

print('start')
if __name__ == '__main__':
    print('main')

    candidates = [1, 2, 3, 4, 5, 6]

    solution = Solution()
    solution.execute(candidates) 

print('stop')