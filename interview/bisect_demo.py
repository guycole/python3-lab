#
# Title:bisect.py
# Description: Demonstrate bisection module.
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Legalise:Copyright (C) 2022 Miserable Bastards, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import bisect

if __name__ == '__main__':
    sorted_fruits = ['apple', 'banana', 'orange', 'plum']
    print(sorted_fruits)

    result = bisect.bisect_left(sorted_fruits, 'banana')
    print(result)

    bisect.insort(sorted_fruits, 'apricot')
    bisect.insort(sorted_fruits, 'watermelon')
    print(sorted_fruits)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
