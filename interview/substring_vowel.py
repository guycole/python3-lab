#
# Title: substring_vowel.py
# Description: how many substrings of only vowels
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/
#
# set operations
# set.union()
# set.intersection()
# set.difference()
# set.symmetric_difference()
# 

class Solution:

    def works(self, word: str) -> int:
        vowels = {"a", "e" , "i", "o", "u"}

        if len(word) < len(vowels):
            return 0

        candidates = []
        for ndx1 in range(len(word)):
            for ndx2 in range(ndx1+1, len(word)):
                temp = word[ndx1:ndx2+1]
                if len(temp) < len(vowels):
                    continue

                test = vowels.symmetric_difference(temp)
                if len(test) == 0:
                    candidates.append(temp)
            
        print(candidates)

        return len(candidates)

    def window(self, word: str) -> int:
        vowels = {"a", "e" , "i", "o", "u"}

        if len(word) < len(vowels):
            return 0

        left = 0
        right = len(word) - len(vowels)

    def countVowelSubstrings(self, word: str) -> int:
        vowel_set = {"a", "e", "i", "o", "u"}

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
    
    def demo(self, word: str) -> int:
        vowel_set = {"a", "e", "i", "o", "u"}

        print(word)
        candidates = set(word)

        print(vowel_set.union(candidates))
        print(vowel_set.intersection(candidates))
        print(vowel_set.difference(candidates)) # only consonants
        print(vowel_set.symmetric_difference(candidates))
        print("-------")
        print(candidates.union(vowel_set))
        print(candidates.intersection(vowel_set))
        print(candidates.difference(vowel_set))
        print(candidates.symmetric_difference(vowel_set))
        print("-------")

        return 0
 
if __name__ == '__main__':
    print("main")

    solution = Solution()

#    print(solution.demo("aeiouu"))
#    print(solution.demo("unicornarihan"))
#    print(solution.demo("cuaieuouac"))

    print(solution.countVowelSubstrings("aeiouu"))
    print(solution.countVowelSubstrings("unicornarihan"))
    print(solution.countVowelSubstrings("cuaieuouac"))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
