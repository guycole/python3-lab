#
# Title:anagram.py
# Description: Demonstrate anagram by sorting.
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

