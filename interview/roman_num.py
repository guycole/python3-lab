#
# Title: topk.py
# Description: discover the top k values
#
class Solution:
    # 1223
    def romanToInt(self, ss: str) -> int:
        result = 0

        consume = 0

        while len(ss) > 0:
            if ss.startswith("IV"):
                result = result + 4
                ss = ss[2:]
            elif ss.startswith("IX"):
                result = result + 9
                ss = ss[2:]
            elif ss.startswith("XL"):
                result = result + 40
                ss = ss[2:]
            elif ss.startswith("XC"):
                result = result + 90
                ss = ss[2:]
            elif ss.startswith("CD"):
                result = result + 400
                ss = ss[2:]
            elif ss.startswith("CM"):
                result = result + 900
                ss = ss[2:]
            elif ss.startswith("I"):
                result = result + 1
                ss = ss[1:]
            elif ss.startswith("V"):
                result = result + 5
                ss = ss[1:]
            elif ss.startswith("X"):
                result = result + 10
                ss = ss[1:]
            elif ss.startswith("L"):
                result = result + 50
                ss = ss[1:]
            elif ss.startswith("C"):
                result = result + 100
                ss = ss[1:]
            elif ss.startswith("D"):
                result = result + 500
                ss = ss[1:]
            elif ss.startswith("M"):
                result = result + 1000
                ss = ss[1:]

        return result
    
if __name__ == '__main__':
    print("main")

    ss = Solution()
    result = ss.romanToInt("III")
    print(result)

    # 58
    result = ss.romanToInt("LVIII")
    print(result)

    # 1994
    result = ss.romanToInt("MCMXCIV")
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
