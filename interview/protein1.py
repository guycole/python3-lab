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
    def start_filter(self, target:int, sequences:Dict[str, tuple]) -> List[str]:
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
        # look for new combinations
        while loop_flag is True:
            derived.clear()

            for key in database.keys():
                print(f"{key} {database[key]}")

                loop_flag = False
                fresh = self.start_filter(database[key][2], database)
                for candidate in fresh:
                    fresh_key = f"{key}_{candidate}"
                    if fresh_key in derived or fresh_key in database:
                        print(f"skipping {fresh_key}")
                    else:
                        print(f"adding {fresh_key}")
                        fresh_tuple = (fresh_key, database[key][1], database[candidate][2])
                        derived.append(fresh_tuple)
                    
            # merge any fresh results into the database
            for candidate in derived:
                loop_flag = True
                database[candidate[0]] = candidate

        # if original values must be excluded
        # test for underbar in database key

        # if sequences must only have longest value
        # i.e. abc_def and def_ghi must be excluded
        # only abc_def_ghi will remain
        # break up string by underbar and delete
        # i.e. abc_def_ghi -> abc_def, def_ghi must be deleted
#        survivor = "abc_def_ghi_jkl"
#        tokens = survivor.split('_')
#       print("-----")
#        print(tokens)
      
#        for ndx1 in range(0, len(tokens)):
#            for ndx2 in range(ndx1+1, len(tokens)):
#                print(f"{ndx1} {ndx2} {len(tokens)} {tokens[ndx1]} {tokens[ndx2]}")
#                buffer1 = tokens[0:ndx1]
#                buffer2 = tokens[ndx2:len(tokens)]
#                print(f"b1:{buffer1} b2:{buffer2}")

#                print(f"{ndx1} {ndx2} {tokens[ndx1]} {tokens[ndx2]}")
#                key = "_".join(tokens[ndx1:ndx2+1])
                #print(key)
#            key = "_".join(tokens[0:ndx+1])
#            print(key)

# abc_def 
# abc_def_ghi
# def_ghi
# def_ghi_jkl
# ghi_jkl

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
