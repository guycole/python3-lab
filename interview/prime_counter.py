#
# Title: prime_counter.py
# Description: how many primes given a upper bound?
# 
# 1641

class Solution:

    # how many primes bounded by limit
    def execute(self, limit: int) -> int:
        print("execute")

        buffer = [True] * limit
        buffer[0] = False
        buffer[1] = False

        # sieve of erastothenes
        # 0, 1, 2, 3, 4, 5 where 2, 3, 5, 7, 11 are primes
        for ndx1 in range(2, limit):
            for ndx2 in range(ndx1, limit, ndx1):
#                print(f"{ndx1} {ndx2}")
                if ndx1 != ndx2:
                    buffer[ndx2] = False

        # print(buffer)

        result = 0
        for ndx1 in range(limit):
            if buffer[ndx1] is True:
                result = 1 + result

        return result

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute(15))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
