#
# Title: csv_demo.py
# Description: csv demonstration 
# 
#
import csv

class Solution:

    def execute(self, file_name: str) -> None:
        with open(file_name, newline='') as infile:
            reader = csv.reader(infile, delimiter=',')
            for row in reader:
                print(row)

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.execute("uhf_anderson.csv")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
