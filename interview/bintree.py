# open ai sample
#
#
#
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val} {self.left} {self.right}"

    def getsum(self) -> int:
        sum = 0

        if self.left is not None:
            sum += self.left.getsum()
        
        sum += self.val

        if self.right is not None:
            sum += self.right.getsum()

        return sum

print('start')
if __name__ == '__main__':
    print('main')

    node1 = Node(val=1)
    node2 = Node(val=2)
    node3 = Node(val=3, left=node1, right=node2)
    node4 = Node(val=4)
    node5 = Node(val=5, left=node4, right=node3)

    print(node3.getsum()) # 6
    print(node5.getsum()) # 15

print('stop')