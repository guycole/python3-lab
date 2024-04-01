#
# Title: substring2.py
# Description: much slower than substring1
#
class Solution:
    def isDistinct(self, ss, ii, jj):
#        print(f"isDistinct {ii} {jj} {ss[ii:jj+1]}")
        
        visited = [False] * (256) # 256 ASCII characters
 
        for kk in range(ii, jj + 1):
            if (visited[ord(ss[kk])] == True):
        #        print(f"match noted {kk} {ss[kk]}")
                return False
 
            visited[ord(ss[kk])] = True

        return True

    def longestUniqueSubString(self, ss):
        limit = len(ss)

        result = 0
 
        for ii in range(limit):
            # print(f"ii {ii} {limit}")
            for jj in range(ii, limit):
                if (self.isDistinct(ss, ii, jj)):
                    result = max(result, jj - ii + 1)
                else:
                    break

        return result

if __name__ == '__main__':
    print("main")

    ss = Solution()
    result = ss.longestUniqueSubString("abcabcbb")
    print(result)

    result = ss.longestUniqueSubString("")
    print(result)

    result = ss.longestUniqueSubString(" ")
    print(result)

    result = ss.longestUniqueSubString("au")
    print(result)

    result = ss.longestUniqueSubString("bbbbb")
    print(result) 

    result = ss.longestUniqueSubString("pwwkew")
    print(result) 

    raw1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    print(f"length of raw1 {len(raw1)}")
    big_string = raw1 * 100
    result = ss.longestUniqueSubString(big_string)
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
