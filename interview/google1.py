#
# Title:google1.py
# Description: Google interview latency tree
#

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return f"{self.value} {self.children}"

class GoogleTree:
    def __init__(self):
        self.max_value = -1

    def add_children(self, current_node, target, children):
#        print(f"entry for {current_node.value}")

        if current_node.value == target:
            print(f"match {target}")
            for child in children:
                current_node.children.append(Node(child))
        else:
            for temp in current_node.children:
                self.add_children(temp, target, children)

    def find_max(self, current, cumulative):
#        print(current.value)

        cumulative += current.value
        if cumulative > self.max_value:
            print(f"new max {cumulative}")
            self.max_value = cumulative

        for temp in current.children:
            self.find_max(temp, cumulative)

if __name__ == '__main__':
    print("main")

    root_node = Node(0)
    print(root_node)

    gt = GoogleTree()
    gt.add_children(root_node, 0, [3, 10, 5])
    print(root_node)

    gt.add_children(root_node, 3, [7, 2])
    print(root_node)

    gt.add_children(root_node, 2, [4, 9])
    print(root_node)

    gt.add_children(root_node, 5, [6])
    print(root_node)

    gt.add_children(root_node, 6, [1])
    print(root_node)

    gt.find_max(root_node, 0)
    print(f"max value {gt.max_value}")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
