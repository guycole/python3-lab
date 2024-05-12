#
# Title: substring5.py
# Description: longest non repeating substring
# 1046 1057

class Solution:
 
    # sliding window 2100
    def execute2(self, candidate: str) -> str:
        print(f"execute2: {candidate}")

        elements = {}
        
        max_substring_length = 0
        max_substring_ndx = -1

        tokens = list(candidate)

        ndx1 = 0
        while ndx1 < len(tokens):
            if tokens[ndx1] in elements:
                # repeater
                if len(elements) > max_substring_length:
                    max_substring_length = len(elements)
                    max_substring_ndx = ndx1 - len(elements)

                ndx1 = elements[tokens[ndx1]] + 1
                elements.clear()
            else:
                # non-repeater
                elements[tokens[ndx1]] = ndx1
                ndx1 = ndx1 + 1

        return candidate[max_substring_ndx:max_substring_ndx+max_substring_length]

    # brute force o(n^2)
    def execute1(self, candidate: str) -> str:
        print(f"execute1: {candidate}")

        elements = {}
        
        max_substring_length = 0
        max_substring_ndx = 0

        tokens = list(candidate)
        for ndx1 in range(len(tokens)):
            elements.clear()
            elements[tokens[ndx1]] = ndx1
            for ndx2 in range(ndx1+1, len(tokens)):
#                print(f"current indices {ndx1} {tokens[ndx1]} {ndx2} {tokens[ndx2]}")
                if tokens[ndx2] in elements:
                    # repeater 
                    if max_substring_length < len(elements):
                        max_substring_length = len(elements)
                        max_substring_ndx = ndx1
                        print(f"new max {max_substring_length} {max_substring_ndx}")
                    break
                else:
                    # non repeater
                    elements[tokens[ndx2]] = ndx2

        return candidate[max_substring_ndx:max_substring_ndx+max_substring_length]

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute2("abcdeab"))
#    print(solution.execute1("abcdeabcdefab"))
#    print(solution.execute1("abcabcbb"))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
