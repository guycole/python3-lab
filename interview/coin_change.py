#
# Title: coin_change.py
# Description: 
# 
# 2332

class Solution:

    def execute(self, amount: float) -> str:
        coins = {
            'quarter': 0,
            'dime': 0,
            'nickel': 0,
            'penny': 0
        }

        results = ""

        cents = int(amount * 100)  
        while cents > 0:
            print(f"current {cents}")
            if cents >= 25:
                cents = cents - 25
                coins['quarter'] = coins['quarter'] + 1
            elif cents >= 10:
                cents = cents - 10
                coins['dime'] = coins['dime'] + 1
            elif cents >= 5:
                cents = cents - 5
                coins['nickel'] = coins['nickel'] + 1 
            else:
                cents = cents - 1
                coins['penny'] = coins['penny'] + 1
            
        #print(coins)
                
        for key, value in coins.items():
            results = results + f"{value} {key} "

        return results

if __name__ == '__main__':
    print("main")

    solution = Solution()
    print(solution.execute(0.91))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
