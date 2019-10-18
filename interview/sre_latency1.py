#
# Title:sre_latency1.py
# Description:
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Legalise:Copyright (C) 2019 Miserable Bastards, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

class Solution:
    def execute(self):
        print('execute')

# replace with
        in_file = open('sre_latency1.dat', 'r')
        raw_buffer = in_file.readlines()
        in_file.close()

# 2018:08:11 19:15:45,PUT,http://example.com/HBLQX74I39,15ms

        results = []

# use negative indices
        for current in raw_buffer:
            tokens = current.strip().split(',')
            latency = tokens[len(tokens)-1]
            print(latency[:len(latency)-2])
            results.append(int(latency[:len(latency)-2]))

        results = sorted(results)
        print(results)
#
# main driver
#
if __name__ == '__main__':
    driver = Solution()
    status = driver.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
