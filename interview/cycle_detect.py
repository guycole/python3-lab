#
# Title: cycle_detect.py
# Description: floyd cycle detection on a single linked list
# 
# 1152 1208

from typing import Dict

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class Solution:

    def execute(self, root: Node) -> bool:
        print("execute")

        tortoise = root
        hare = root.next

        while True:
            if tortoise is None or hare is None:
                print("none noted")
                break

            print(f"{tortoise.value} {hare.value}")

            if tortoise == hare:
                print("match noted")
                return True

            tortoise = tortoise.next
            hare = hare.next
            if hare is not None:
                hare = hare.next

        return False

if __name__ == '__main__':
    print("main")

    root = Node(9)
    current = root
    current.next = Node(7)
    current = current.next
    current.next = Node(4)
    current = current.next
    looper = current
    current.next = Node(3)
    current = current.next
    current.next = Node(8)
    current = current.next
    current.next = Node(1)
    tail = current.next 

#    temp = root
#    while temp is not None:
#        print(temp.value)
#        temp = temp.next

    solution = Solution()
    print(solution.execute(root))

    tail.next = looper
    print(solution.execute(root))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
