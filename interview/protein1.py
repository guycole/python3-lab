#
# Title: protein1.py
# Description: generate protein sequences
# 
#https://leetcode.com/discuss/interview-question/3229839/Benchling-or-Phone-or-Generate-Protein
#https://leetcode.com/discuss/interview-question/1386125/Benchling-Phone-interview
#
from typing import Dict, List

class Solution:
 
    # return a list of keys with start index equal to target, i.e. ['e5c', 'xxx']
    def _start_filter(self, target:int, sequences:Dict[str, tuple]) -> List[str]:
        results = [key for key, value in sequences.items() if value[1] == target]
        return results

    # this version returns intermediate results i.e. abc_def, def_ghi, abc_def_ghi
    def execute1(self, sequences: List[tuple]) -> List[tuple]:
        # convert list of tuples to dictionary
        database = {}
        for candidate in sequences:
            database[candidate[0]] = candidate

        derived = []
        loop_flag = True
        # discover for new combinations
        while loop_flag is True:
            derived.clear()
            loop_flag = False # reset if new combinations are discovered
          
            for key in database.keys():
                print(f"top of key loop {key} {database[key]}")
   
                fresh = self._start_filter(database[key][2], database)
                for candidate in fresh:
                    fresh_key = f"{key}_{candidate}"

                    if fresh_key in database.keys():
                        print(f"skipping {fresh_key}")
                    else:
                        print(f"adding {fresh_key}")
                        derived.append((fresh_key, database[key][1], database[candidate][2]))

            # merge any fresh results into the database
            for candidate in derived:
                print(f"database merge {candidate}")
                loop_flag = True
                database[candidate[0]] = candidate

        # if original values must be excluded
        # test for underbar in database key

        # print(database)
        results = []
        for key in database.keys():
            results.append(database[key])

        return results

if __name__ == '__main__':
    print("main")

    # tuple name, start, end
    sequences3 = [('acG', 0, 5), ('Bf5', 0, 22), ('e5c', 5, 16), ('7f6c', 2, 13), ('0Pf', 13, 23), 
                 ('0f5c', 0, 13), ('yyy', 7, 17), ('xxx', 5, 7),
                 ('abc', 0, 4), ('def', 4, 7), ('ghi', 7, 9)]
    
    sequences2 = [('acG', 0, 5), ('Bf5', 0, 22), ('e5c', 5, 16), ('7f6c', 2, 13), ('0Pf', 13, 23), 
                 ('0f5c', 0, 13), ('abc', 0, 4), ('def', 4, 7), ('ghi', 7, 9)]
    
    sequences1 = [('acG', 0, 5), ('Bf5', 0, 22), ('e5c', 5, 16), ('6a5d', 5, 17), ('7f6c', 2, 13),  
                  ('0Pf', 13, 23), ('0f5c', 0, 13), ('abc', 0, 4), ('def', 4, 7), ('ghi', 7, 9)]
 
    #print(type(sequences[0]))

    solution = Solution()
    result = solution.execute1(sequences1)
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
