#
# Title:iterator1.py
# Description: iterator demo
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Legalise:Copyright (C) 2019 Miserable Bastards, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

class BoundedRepeater:
    def __init__(self, value, maxx):
        self.maxx = maxx
        self.ndx = 0
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.ndx >= self.maxx:
            raise StopIteration

        self.ndx += 1

        return self.value

if __name__ == '__main__':
    print("main")

    repeater = BoundedRepeater('Hello', 3)
    for item in repeater:
        print(item)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
