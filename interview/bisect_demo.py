#
# Title:bisect.py
# Description: Demonstrate bisection module.
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
