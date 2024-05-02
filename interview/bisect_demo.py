#
# Title:bisect.py
# Description: Demonstrate bisection module.
#
import bisect

if __name__ == '__main__':
    sorted_fruits = ['apple', 'banana', 'orange', 'plum']
    print(sorted_fruits)

    # insert before banana, use bisect_right for after banana
    result = bisect.bisect_left(sorted_fruits, 'banana')
    print(result)

    # insort is O(n)
    bisect.insort(sorted_fruits, 'apricot')
    bisect.insort(sorted_fruits, 'watermelon')
    print(sorted_fruits)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
