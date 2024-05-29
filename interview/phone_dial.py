#
# Title: phone_dial.py
# Description: discover strings from phone dial
#
from typing import List

class Solution:
    def converter(self, candidates: List[str], indices: List[int]) -> str:
        result = ""
        for ndx1 in range(len(indices)):
            result = result + candidates[ndx1][indices[ndx1]]
        return result
    
    def sequencer(self, candidates: List[str]) -> List[int]:
        print(candidates)

        limit = []
        total = 1
        for candidate in candidates:
            limit.append(len(candidate))
            total = total * len(candidate) 
#        print(limit)
#        print(total)

        current = [0]*len(candidates)

        indices = []
        indices.append(current.copy())

        for ndx1 in range(total):
            indices.append(current.copy())
    
        for ndx1 in range(1, total):
#            print(current)

            carry = 1
            digit_ndx = len(candidates)

            while carry > 0:
                digit_ndx = digit_ndx - 1
#                print(f"incrementing: {digit_ndx}")

                temp = current[digit_ndx]
                temp = temp + 1

                if temp >= limit[digit_ndx]:
                    carry = 1
                    current[digit_ndx] = 0
                else:
                    carry = 0
                    current[digit_ndx] = temp

                indices[ndx1] = current.copy()

        return indices

    def letterCombinations(self, digits: str) -> List[str]:
        keys = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        if len(digits) < 1:
            return []

        if len(digits) < 2:
            return(list(keys[digits[0]]))

        candidates = []
        for ndx1 in list(digits):
            candidates.append(keys[ndx1])

        indices = self.sequencer(candidates)  
#        print(indices)

        results = []
        for ndx in indices:
            results.append(self.converter(candidates, ndx))
        
        return results

if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("237"))
    #print(solution.letterCombinations("3910057"))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
