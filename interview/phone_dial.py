#
# Title: phone_dial.py
# Description: discover strings from phone dial
#

class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
        keys = {"0": "", "1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        if len(digits) < 1:
            return []

        if len(digits) < 2:
            return(list(keys[digits[0]]))

        digitz = [] # digits with characters 
        characterz = [] # characters for each digit
        for ndx1 in range(len(digits)):
            temp = keys[digits[ndx1]]
            if len(temp) > 0:
                digitz.append(digits[ndx1])
                characterz.append(temp)

        # each character entry has an index
        indicez = [0] * len(digitz)

        print(digitz)
        print(indicez)
        print(characterz)

        results = []

        while True:
            # print(indicez)

            # build a string from the indices
            buffer = []
            for temp in range(len(indicez)):
                buffer.append(characterz[temp][indicez[temp]])
#                print(buffer)

            results.append("".join(buffer))

            # index management
            for temp in range(len(indicez)-1 , -1, -1):
                indicez[temp] = indicez[temp] + 1
                if indicez[temp] >= len(characterz[temp]):
                    indicez[temp] = 0
                else:
                    break

            if sum(indicez) == 0:
                break

        return results

if __name__ == '__main__':
    solution = Solution()
    #print(solution.letterCombinations("2"))
    #print(solution.letterCombinations("234"))
    #print(solution.letterCombinations("3910057"))
    results = solution.letterCombinations("5936963")
    print(results)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
