#
# Title: protein2.py
# Description: 
# 
#https://leetcode.com/discuss/interview-question/3229839/Benchling-or-Phone-or-Generate-Protein
#https://leetcode.com/discuss/interview-question/1386125/Benchling-Phone-interview
#

from typing import List


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

    def execute(self) -> List[tuple]:
        print("execute")

        results = []

        for key in self.protein.keys():
            print(f"{key} {self.protein[key]}")
            value = self.protein[key]

            last_tuple = None
            start_tuple = None
            fail_flag = False

            # keys must ordered by start index
            for ndx in key:
                sequence = self.sequences[ndx]

                if last_tuple is None:
                    last_tuple = sequence
                    start_tuple = sequence
                else:
                    if last_tuple[1] == sequence[0]:
                        last_tuple = sequence
                    else:
                        print(f"fail {value} {last_tuple} {sequence}")
                        fail_flag = True
                        break

            if fail_flag is False:
                temp_tuple = (value, start_tuple[0], last_tuple[1])
                results.append(temp_tuple)  

        #print(results)

        return results

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute())

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
