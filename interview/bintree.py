# open ai sample
#
#
#
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def getsum(self) -> int:
        sum = 0

        while self.left is not None:
            self = self.left
            sum += self.val

        while self.right is not None:
            self = self.right
            sum += self.val

        return sum


print('start')
if __name__ == '__main__':
    print('main')

    node1 = Node(val=1)
    node2 = Node(val=2)
    node3 = Node(val=3, left=node1, right=node2)

    print(node3.getsum()) # 6

print('stop')