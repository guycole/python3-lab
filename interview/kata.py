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

        # demo list
        targets = ['a', 'b', 'c']

        # visit each pair of targets
        for ndx1 in range(len(targets)):
            for ndx2 in range(ndx1+1, len(targets)):
                print(f"{targets[ndx1]}, {targets[ndx2]}")    

        # make string from list
        print("".join(targets))

        # reverse a string/list
        revtargets = targets[::-1]
        print(revtargets)
        print(revtargets[::-1])

        # reverse a string/list
        buffer = []
        for ndx1 in range(len(targets)-1, -1, -1):
            buffer.append(targets[ndx1])
        
        print(buffer)

        # list comprehension
        lc = [x*x for x in range(10) if x % 2 == 0]
        print(lc)

        dd = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 2
        }

        print(dd)
        results = [key for key, value in dd.items() if value == 2]
        print(results)

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

    def execute(self, file_name: str) -> None:
        print("execute")

        self.kata()

        # use substring5.py example
        # use subset1.py example

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.execute("json_reader.json")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
