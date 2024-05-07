# binary tree example
# insertion is O(h) where h is the height of the tree
# search is O(log n) for balanced tree
#

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __eq__(self, other):
        try:
            return (self.value) == (other.value)
        except AttributeError:
            return NotImplemented

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"{self.left} {self.value} {self.right}"
    
    def __str__(self):
        return f"{self.value}"

class BinTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def insert(self, value):
        candidate = Node(value)

        print(f"insert {value}")

        if self.root is None:
            self.root = candidate
        else:
            current = self.root
            flag = True
            while flag:
                if candidate.value < current.value:
                    if current.left is None:
                        current.left = candidate
                        flag = False
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = candidate
                        flag = False
                    else:
                        current = current.right

    def find(self, target):
        current = self.root
        while current.value != target:
            if target < current.value:
                print("left")
                current = current.left
            else:
                print("right")
                current = current.right

        print("matched")
        return current

    def preorder(self, current):
        if current.left is not None:
            self.preorder(current.left)

        print(current.value)

        if current.right is not None:
            self.preorder(current.right)

    def postorder(self, current):
        if current.left is not None:
            self.postorder(current.left)

        if current.right is not None:
            self.postorder(current.right)

        print(current.value)

    def inorder(self, current):
        if current.left is not None:
            self.inorder(current.left)

        print(current.value)

        if current.right is not None:
            self.inorder(current.right)

print('start')
if __name__ == '__main__':
    print('main')

    bintree = BinTree()
    bintree.insert(5)
    bintree.insert(3)
    bintree.insert(1)
    bintree.insert(9)
    bintree.insert(7)
    bintree.insert(4)
    print(bintree)

    xx = bintree.find(7)

    print("-x- preorder -x-")
    bintree.preorder(bintree.root)

    print("-x- postorder -x-")
    bintree.postorder(bintree.root)

    print("-x- inorder -x-")
    bintree.inorder(bintree.root)

print('stop')