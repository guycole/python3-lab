#
# Title: hanoi.py
# Description: towers of hanoi
#
from typing import TypeVar, Generic, List, Dict

T = TypeVar('T')

class Stack(Generic[T]):
    # from Classic Computer Science Problems in Python

    def __init__(self) -> None: 
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)

class Hanoi:

    def hanoi(self, begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
        # print(f"{begin} {end} {temp} {n}")

        if n == 1:
            end.push(begin.pop())
        else:
            self.hanoi(begin, temp, end, n - 1)
            self.hanoi(begin, end, temp, 1)
            self.hanoi(temp, end, begin, n - 1)

    def execute(self, disk_limit: int, peg_limit: int):
        print("execute")

        peg_a = Stack()
        peg_b = Stack()
        peg_c = Stack()

        for ndx in range(disk_limit):
            peg_a.push(ndx)

        print(peg_a)

        self.hanoi(peg_a, peg_b, peg_c, disk_limit)

        print(peg_a)
        print(peg_b)
        print(peg_c)

if __name__ == '__main__':
    print("main")

    hanoi = Hanoi()
    hanoi.execute(3, 3)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
