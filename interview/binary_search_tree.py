# binary search tree example
#
# balanced vs unbalanced, no duplicate keys
# insertion is O(h) where h is the height of the tree
# search is O(log n) for balanced tree
#
# there is a "binarytree" module
#
import queue

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
        while current is not None: 
            if current.value == target:
                print("matched")
                return current
            if target < current.value:
                print("left")
                current = current.left
            else:
                print("right")
                current = current.right

        print("match failure")
        return None

    def preorder(self, current):
        print(current.value)

        if current.left is not None:
            self.preorder(current.left)
        
        if current.right is not None:
            self.preorder(current.right)
        
#        print(f"pop {current.value}")

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

#        print(f"pop {current.value}")

    def breadth_first(self, root):
        qq = queue.Queue()
        qq.put(root)

        current = None
        while not qq.empty():
            current = qq.get()
            print(current.value)

            if current.left:                  
                qq.put(current.left)
            if current.right:
                qq.put(current.right)

    # only one node has height one
    # find deepest node and count to root
    def height(self, root):
        if root is None:
            return 0
        else:
            height = 1 + max(self.height(root.left), self.height(root.right))
#            print(f"height {height} {root}")

        return height

print('start')
if __name__ == '__main__':
    print('main')

    bintree = BinTree()
    candidates = [5, 3, 1, 9, 7, 4, 6]
    for candidate in candidates:
        bintree.insert(candidate)

    print(bintree)

    xx = bintree.find(7)
    xx = bintree.find(44)

    print("-x- preorder -x-")
    bintree.preorder(bintree.root)

    print("-x- postorder -x-")
    bintree.postorder(bintree.root)

    print("-x- inorder -x-")
    bintree.inorder(bintree.root)

    print("-x- breadth first -x-")
    bintree.breadth_first(bintree.root)

    print("-x- height -x-")
    print(bintree.height(bintree.root))

print('stop')
