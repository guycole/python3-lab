#
# Title:double_list.py
# Description: classic linked list
#

class Node:
    def __init__(self, payload, next=None, last=None):
        self.payload = payload
        self.next = next
        self.last = last

    def __repr__(self):
        return self.payload


class DoubleLinkedList:
    def __init__(self):
        self.root = None

    def __repr__(self):
        buffer = ''
        current = self.root
        while current:
            buffer += current.payload
            current = current.next

        return buffer

    def add(self, payload):
        node = Node(payload)

        # why not add to front?

        if self.root:
            current = self.root

            while current.next:
                current = current.next

            current.next = node
            node.last = current
        else:
            self.root = node


class SingleLinkedList:
    def __init__(self):
        self.root = None

    def __repr__(self):
        buffer = ''
        current = self.root
        while current:
            buffer += current.payload
            current = current.next

        return buffer

    def add(self, payload):
        node = Node(payload)

        # why not add to front?

        if self.root:
            current = self.root
            while current.next:
                current = current.next

            current.next = node
        else:
            self.root = node

if __name__ == '__main__':
    print("main")

    singleLinkedList = SingleLinkedList()
    singleLinkedList.add('a')
    singleLinkedList.add("b")
    singleLinkedList.add("c")

    print(singleLinkedList)

    doubleLinkedList = DoubleLinkedList()
    doubleLinkedList.add('a')
    doubleLinkedList.add("b")
    doubleLinkedList.add("c")
    doubleLinkedList.add("d")

    print(doubleLinkedList)

    current2 = doubleLinkedList.root
    while current2:
        print(current2)
        last = current2
        current2 = current2.next

    print("----------")

    while last:
        print(last)
        last = last.last

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
