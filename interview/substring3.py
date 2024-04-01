#
# Title: substring3.py
# Description: sliding window for nonrepeating chars in O(n^2)
#
class Solution:
    def longestUniqueSubString(self, ss):
        limit = len(ss)
        result = 0
  
        for ii in range(limit):
            visited = [False] * 256  

            for jj in range(ii, limit):
                if (visited[ord(ss[jj])] == True):
                    break 
                else:
                    result = max(result, jj - ii + 1)
                    visited[ord(ss[jj])] = True

            visited[ord(ss[ii])] = False
     
        return result

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
    result = ss.longestUniqueSubString(big_string)
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
