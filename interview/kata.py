#
# Title: kata.py
# Description: 
# 
#

from typing import Dict


class Solution:

    def kata(self) -> None:
        print("kata")

        # visit each pair of targets

        targets = ['a', 'b', 'c']

        for ndx1 in range(len(targets)):
            for ndx2 in range(ndx1+1, len(targets)):
                print(f"{targets[ndx1]}, {targets[ndx2]}")    

        # make string from list
        yy = "".join(targets)
        print(yy)

        # reverse a string/list
        revtargets = targets[::-1]
        print(revtargets)
        print(revtargets[::-1])

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
            with open("json_reader.json", "r") as file:
                print(file.read())
        except Exception as error:
                print(error)

        return

    def execute(self, file_name: str) -> None:
        print("execute")

        self.kata()

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.execute("json_reader.json")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
