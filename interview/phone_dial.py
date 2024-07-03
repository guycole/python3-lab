#
# Title: phone_dial.py
# Description: discover strings from phone dial
#

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

    def letterCombinations(self, digits: str) -> list[str]:
        keys = {"0": "", "1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        if len(digits) < 1:
            return []

        if len(digits) < 2:
            return(list(keys[digits[0]]))

        digitz = []
        characterz = []
        for ndx1 in range(len(digits)):
            temp = keys[digits[ndx1]]
            if len(temp) > 0:
                digitz.append(digits[ndx1])
                characterz.append(temp)

        indicez = [0] * len(digitz)

        print(digitz)
        print(indicez)
        print(characterz)

#        indices = []
#        for ndx1 in range(len(digits)):
#            indices.append(0)


#        candidates = []
#        for ndx1 in list(digits):
#            if len(keys[ndx1]) > 0:
#                candidates.append(keys[ndx1])

#        print(candidates)

#        indices = self.sequencer(candidates)  
#        print(indices)
#        print(len(indices))

        results = []
#        for ndx in indices:
#            temp = self.converter(candidates, ndx)
#            if temp not in results:
#                results.append(temp)

#        print(len(results))

        return results

if __name__ == '__main__':
    solution = Solution()
    #print(solution.letterCombinations("2"))
    print(solution.letterCombinations("234"))
    #print(solution.letterCombinations("3910057"))
    #results = solution.letterCombinations("4085936964")
    #print(results)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
