#
# Title:anagram.py
# Description: Demonstrate anagram by sorting.
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Legalise:Copyright (C) 2019 Miserable Bastards, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

if __name__ == '__main__':
    candidate1 = "bogus"
    candidate2 = "bogus"

    sorted1 = ''.join(sorted(candidate1))
    sorted2 = ''.join(sorted(candidate2))


    if sorted1 == sorted2:
        print("anagram")
    else:
        print("not anagram")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***

