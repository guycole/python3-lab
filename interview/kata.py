#
# Title: kata.py
# Description: interview drill 
# 5 minutes to replicate from memory
#

class Solution:

    def kata(self) -> None:
        print("kata")

        # initialize array
        dummy = [0] * 10

        # shallow list copy
        dummy2 = dummy[:] # slicing
        dummy3 = dummy.copy()
        dummy4 = list(dummy)

        # sorts list in place O(n log n)
        #list.sort()

        # returns new list O(n log n) timsort
        # sorted(iterable)

        # demo list
        targets = ['a', 'b', 'c']

        # visit each pair of targets
        for ndx1 in range(len(targets)):
            for ndx2 in range(ndx1+1, len(targets)):
                print(f"{targets[ndx1]}, {targets[ndx2]}")    

        # make string from list
        print("".join(targets))

        # reverse a string/list
        revtargets = targets[::-1] # slicing start:stop:step
        print(revtargets)
        print(revtargets[::-1])

        # reverse a string/list
        buffer = []
        for ndx1 in range(len(targets)-1, -1, -1):
            buffer.append(targets[ndx1])
        
        print(buffer)

        # list comprehension
        lc = [x*x for x in range(11) if x % 2 == 0]
        print(lc)

        dd = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
        print(dd)

        # iterate for all dictionary keys
        for key in dd.keys():
            print(f"{key} {dd[key]}")

        # iterate for all dictonary key, value pairs (returns tuple)
        for key, value in dd.items():
            print(f"key: {key} value: {value}")

        # iterate for all dictionary values
        for value in dd.values():
            print(f"{value}")

        # list comprehension to select keys with value 2
        selected = [key for key, value in dd.items() if value == 2]
        print(selected)

        # sort dictionary by value, returns list of tuples by descending value returns new list O(n log n)
        # sorted(iterable, key=key, reverse=reverse) 
        results = sorted(dd.items(), key=lambda xx: xx[1], reverse=True)
        print(f"{results}")

        # dictionary comprehension to sort dictionary by descending value
        # sorted(iterable, key=key, reverse=reverse)
        results = {key: value for key, value in sorted(dd.items(), key=lambda xx: xx[1], reverse=True)}
        print(results)

        # iterate for all SORTED dictionary keys
        for key in results.keys():
            print(f"{key} {results[key]}")

        # read a file
        try:
            with open("json_reader.json", "r") as infile:
                print(infile.read())
        except Exception as error:
            print(error)

        # 2d array
        matrix = [[1, 2, 3], [4, 5, 6]]
        print(matrix)
        print(len(matrix)) # returns row population
        print(len(matrix[0])) # returns column population

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                print(matrix[row][col], end=" ")

            print()

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.kata()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
