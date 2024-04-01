#
# Title: palindroime.py
# Description: find largest palindrome
#
class Solution:
 
    def is_palindrome(self, candidate:str) -> bool:
        if len(candidate) == 1:
            return True

        reversed = candidate[::-1]
        if candidate == reversed:
            return True

        return False

    def longestPalindrome(self, ss: str) -> str:
        candidates = {}
        winner = ""
        window = 0

        # discover all substrings
        for ndx1 in range(len(ss)):
            for window in range(1, len(ss)-ndx1+1):
                print(f"ndx1: {ndx1} window: {window} ss: {ss[ndx1:ndx1+window]}")
                if ss[ndx1:ndx1+window] not in candidates:
                    candidates[ss[ndx1:ndx1+window]] = len(ss[ndx1:ndx1+window])

        print(candidates)
        print(len(candidates))
        tweaked = {k: v for k, v in sorted(candidates.items(), key=lambda item: item[1], reverse=True)}
    
        for kk, vv in tweaked.items():
            print(f"k: {kk} v: {vv}")
            if self.is_palindrome(kk):
                print(f"winnder: {kk}")
                return kk

if __name__ == '__main__':
    print("main")

    ss = Solution()
    result = ss.longestPalindrome("babad")
    print(result)

    result = ss.longestPalindrome("cbbd")
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
