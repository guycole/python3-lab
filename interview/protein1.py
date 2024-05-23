#
# Title: template.py
# Description: 
# 
#

from typing import Dict


class Solution:
    sequences = {
        'AC': (5, 15),
        'BC': (3, 20),
        'PQ': (15, 22),
        'XY': (22, 35),
        'AB': (20, 32),
        'BT': (9, 13)
    }

    protein = {
        ('AC', 'PQ'): 'P1',
        ('AC','PQ','XY'): 'P2',
        ('BC', 'AB'): 'P3',
        ('BT', 'AC') : 'P4'
    }

    def generateProtein(self, sequences, proteins):
        res = []

        for sNames, pName in proteins.items():
            sNums1, sNums2 = list(zip(*map(sequences.get, sNames)))
            print(sNums1, sNums2)
            if sNums1[1:] == sNums2[:-1]:
                res.append((pName, sNums1[0], sNums2[-1]))
        
        return res

    def execute(self, file_name: str) -> None:
        print("execute")

        print(self.generateProtein(self.sequences, self.protein))

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.execute("json_reader.json")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
