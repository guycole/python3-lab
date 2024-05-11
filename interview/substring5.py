#
# Title: substring5.py
# Description: longest non repeating substring
# 1046 1057

class Solution:
 
    def execute(self, candidate: str) -> str:
        print(f"execute: {candidate}")

        elements = {}
        
        max_substring_length = 0
        nax_substring_ndx = -1

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
                        nax_substring_ndx = ndx1
                        print(f"new max {max_substring_length} {nax_substring_ndx}")
                    break
                else:
                    # non repeater
                    elements[tokens[ndx2]] = ndx2

        return candidate[nax_substring_ndx:nax_substring_ndx+max_substring_length]

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute("abcdeab"))
    print(solution.execute("abcdeabcdefab"))
    print(solution.execute("abcabcbb"))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
