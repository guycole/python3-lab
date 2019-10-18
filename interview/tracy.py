#!/usr/bin/python
#
# Title:tracy.py
#

class Solution:

    def iterative(self, limit, seed_length, candidates):
        for ndx1 in range(limit):
            candidate = 0
            for ndx2 in range(ndx1, ndx1+seed_length):
                candidate += candidates[ndx2]

            candidates.append(candidate)

        return candidates

    def recursive(self, limit, seed_length, candidates):
        if limit > 0:
            list_length = len(candidates)

            candidate = 0
            for ndx in range(list_length-seed_length, list_length):
                candidate += candidates[ndx]

            candidates.append(candidate)

            candidates = self.recursive(limit-1, seed_length, candidates)

        return candidates

if __name__ == '__main__':
    term_limit = 6
    seed = [1, 1, 1]

    driver = Solution()

    result = driver.iterative(term_limit, len(seed), seed.copy())
    print(result)

    result = driver.recursive(term_limit, len(seed), seed.copy())
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***