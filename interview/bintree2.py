# binary tree example
#
# balanced vs unbalanced, no duplicate keys
# insertion is O(h) where h is the height of the tree
# search is O(log n) for balanced tree
#
# demonstrate binary tree module
#
from binarytree import bst, build


print('start')
if __name__ == '__main__':
    print('main')

    nodes = [5, 3, 1, 9, 7, 4, 2]

    bintree = build(nodes)
    print(bintree)
    print(bintree.values)

print('stop')