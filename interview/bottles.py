#
# Title: bottles.py
# Description:  bottle exchange (incomplete)
# 
#
class Solution:
    def numWaterBottles3(self, numBottles: int, numExchange: int) -> int:

        def exchange(numBottles, numExchange):
            print(f"exchange {numBottles} {numExchange}")
            if numBottles < numExchange:
                return 0

            newBottles = numBottles // numExchange
            remainder = numBottles % numExchange

            return newBottles + exchange(newBottles + remainder, numExchange)

        return numBottles + exchange(numBottles, numExchange)
    
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            newBottles = empty // numExchange
            remainder = empty % numExchange
            total += newBottles
            empty = newBottles + remainder

        return total

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.numWaterBottles(9, 3)) # 13

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***