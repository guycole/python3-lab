#
# Title: substring4.py
# Description: sliding window for nonrepeating chars in O(n)
#
class Solution:
    def longestUniqueSubString(self, ss):
        last_idx = {}
        start_idx = 0

        max_len = 0
 
        for ii in range(0, len(ss)):
#            print(f"top {ii}")

            if ss[ii] in last_idx:
#                print(f"cache hit {ss[ii]} {last_idx}")
                start_idx = max(start_idx, last_idx[ss[ii]] + 1)
 
            max_len = max(max_len, ii-start_idx + 1)
#            print(f"{max_len} {start_idx} {ii} {ss[ii]}")
 
            last_idx[ss[ii]] = ii

#        print(last_idx)

        return max_len
 

if __name__ == '__main__':
    print("main")

    ss = Solution()
    result = ss.longestUniqueSubString("abcabcbb")
    print(result)
   
#    result = ss.longestUniqueSubString("")
#    print(result)

#    result = ss.longestUniqueSubString(" ")
#    print(result)

#    result = ss.longestUniqueSubString("au")
#    print(result)

#    result = ss.longestUniqueSubString("bbbbb")
#    print(result) 

#    result = ss.longestUniqueSubString("pwwkew")
#    print(result) 

    raw1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    print(f"length of raw1 {len(raw1)}")
    big_string = raw1 * 100
#    result = ss.longestUniqueSubString(big_string)
#    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
