# Given two strings s and t of lengths n and m respectively,
# return the minimum substring of s such that every character in t
# (including duplicates) is included in the substring.
# If there is no such substring, return the empty string "".

# Input: s = "CODEBANC", t = "ABC"
# CODEBA, BANC
# Output: "BANC"

# C, CO, COD .... O, OD, ODE, ...
# 

def matcher(s, t: str) -> str:
    # t is short string
    # s is long string
    # iterate for t (and subset of t)
    # test for existence in s

    candidates = []

    t_set = set(list(t))

    # generate all possible candidates
    for ndx1 in range(len(s)):
        for ndx2 in range(ndx1+1, len(s)):
            candidates.append(s[ndx1:ndx2+1])

    # print(candidates)

    result = None

    for ndx3 in candidates:
        if len(ndx3) < len(t):
            continue

        if t_set.issubset(ndx3): 
            if result is None:
                result = ndx3
            else:
                if len(result) > len(ndx3):
                    result = ndx3
        
#        satisfied = True
#        for el in t_set:
#            if el in ndx3:
#                continue
#            else:
#                satisfied = False
#
#        if satisfied is True and (result is None or len(result) > len(ndx3)):
#            result = ndx3

    return result

result = matcher("CODEBANC", "ABC")
if result is None:
    print("none result")
else:
    print(result)
