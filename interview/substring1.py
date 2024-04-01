#
# Title: substring1.py
# Description: brute force O(n^2) find the longest substring without repeating characters
#
class Solution:
    def lengthOfLongestSubstring(self, ss: str) -> int:
        limit = len(ss)

        if limit < 2:
            return limit

        candidates = []
        winner = -1
    
        for ndx1 in range(limit):
            candidates.clear()

#            print(f"{ndx1} {limit}")
            for ndx2 in range(ndx1, limit):
#                print(f"{ndx2} {limit}")
                if ss[ndx2] in candidates:
                    break;
                else:
                    candidates.append(ss[ndx2])
                    temp = len(candidates)
                    if temp > winner:
                        winner = temp

        return winner

if __name__ == '__main__':
    print("main")

    ss = Solution()
    result = ss.lengthOfLongestSubstring("abcabcbb")
    print(result)

    result = ss.lengthOfLongestSubstring("")
    print(result)

    result = ss.lengthOfLongestSubstring(" ")
    print(result)

    result = ss.lengthOfLongestSubstring("au")
    print(result)

    raw1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    print(f"length of raw1 {len(raw1)}")
    big_string = raw1 * 100
    result = ss.lengthOfLongestSubstring(big_string)
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
