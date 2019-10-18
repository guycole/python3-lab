#
# Title:single_linked.py
# Description: single linked list
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Legalise:Copyright (C) 2019 Miserable Bastards, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class SingleLinkedList:
    def __init__(self):
        self.root = None

    def insert(self, node):
        node.next = self.root
        self.root = node

    def dumper(self):
        current = self.root
        while current is not None:
            print(f"{current.value}")
            current = current.next

if __name__ == '__main__':
    print("main")

    sll = SingleLinkedList()

    print("-x-x-x-")
    sll.insert(Node(5))
    sll.insert(Node(7))
    sll.insert(Node(9))
    print("-x-x-x-")
    sll.dumper()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***

