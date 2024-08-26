#
# Title: ip_address.py
# Description: convert dotted IPv4 addres
# 
#

class Solution:

    def execute(self, candidate: str) -> None:
        print("execute")

        tokens = candidate.split(".")
        power = len(tokens) - 1
        sum = 0
        for token in tokens:
            temp = int(token)*256**power
            sum += temp

#            print("temp: ", temp)
#            print("token: ", token)
#            print("power: ", power)
            power -= 1

        print("sum: ", sum)

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.execute("172.16.254.1") # 2886794753
#    solution.execute("192.168.1.1") # 3232235777

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
