#
# Title: protein3.py
# Description: generate protein sequences
# 
#https://leetcode.com/discuss/interview-question/3229839/Benchling-or-Phone-or-Generate-Protein
#https://leetcode.com/discuss/interview-question/1386125/Benchling-Phone-interview
#
class Solution:

    def _tuple_test(self, first_tuple:tuple, second_tuple:tuple) -> tuple:
        """ discover if two tuples can be combined, returns None or a new tuple """
        fresh_key = f"{first_tuple[0]}_{second_tuple[0]}"
        #print(f"fresh_key {fresh_key}")

        if first_tuple[2] == second_tuple[1]:
            return (fresh_key, first_tuple[1], second_tuple[2])

        return None

    # this version only makes one pass through the sequences list
    def execute1(self, sequences: list[tuple]) -> list[tuple]:
        """ generate protein sequences """
        database = {}
        # dictionary key is the protein name, value is the tuple
        for candidate in sequences:
            database[candidate[0]] = candidate

        # iterate over list does not lock dictionary, and it is safe to add new keys
        key_list = list(database.keys())
        # O(n^2) run complexity
        for ndx1 in range(len(key_list)):
            for ndx2 in range(ndx1+1, len(key_list)):
                candidate = self._tuple_test(database[key_list[ndx1]], database[key_list[ndx2]])
                if candidate is not None:
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
