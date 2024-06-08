#
# Title: heap_sort.py
# Description: build heap then remove in order
# time complexity O(n logn) slower than quickwortt
# space complexity O(1)
#
# 1. build max heap
# 2. extract element from heap in sorted order
#


class Solution:

    def heapify(self, heap:list[int], limit:int, ndx:int) -> None:
        #print(f"heapify {heap} {limit} {ndx}")
        maximum = ndx

        left = 2 * ndx + 1
        right = 2 * ndx + 2

        # if left child exists
        if left < limit and heap[ndx] < heap[left]:
            maximum = left

        # if right child exists
        if right < limit and heap[maximum] < heap[right]:
            maximum = right

        # root
        if maximum != ndx:
            #print(f"swap {heap[ndx]} {heap[maximum]}")
            heap[ndx], heap[maximum] = heap[maximum], heap[ndx] # swap root
            self.heapify(heap, limit, maximum)

    def heap_sort(self, heap:list[int]) -> None:
        print(f"start {heap}")

        limit = len(heap)

        # maxheap
        for ndx in range(limit, -1, -1):
            self.heapify(heap, limit, ndx)

        print(f"maxheap {heap}")

        # element extraction
        for ndx in range(limit-1, 0, -1):
            heap[ndx], heap[0] = heap[0], heap[ndx]
            self.heapify(heap, ndx, 0)

        print(f"extract {heap}")

    def execute(self, candidates: list[int]) -> None:
        print(f"execute {candidates}")

        self.heap_sort(candidates)
        print(candidates)

        results = []

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.execute([12, 3, 9, 14, 10, 18, 8, 23])

    heap = [4, 3, 1, 0, 2]

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
