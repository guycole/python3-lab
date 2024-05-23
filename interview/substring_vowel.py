#
# Title: substring_vowel.py
# Description: how many substrings of only vowels
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/
# 

class Solution:

    def countVowelSubstrings(self, word: str) -> int:
        vowel_set = {"a", "e" , "i", "o", "u"}

        if len(vowel_set.intersection(word)) < len(vowel_set):
            return 0

        counter = 0
        candidates = list(word)
        for ndx1 in range(0, len(word)-len(vowel_set)+1):
            for ndx2 in range(ndx1, len(word)-len(vowel_set)+1):
                temp = candidates[ndx1:ndx2+len(vowel_set)]
#                print(temp)
#                print(vowel_set.symmetric_difference(temp))
                if len(vowel_set.symmetric_difference(temp)) == 0:
                    counter = counter+1

        return counter
 
if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.countVowelSubstrings("aeiouu"))
    print(solution.countVowelSubstrings("unicornarihan"))
    print(solution.countVowelSubstrings("cuaieuouac"))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
