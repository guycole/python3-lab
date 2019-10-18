#
# Title:one53.py
# Description:
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Legalise:Copyright (C) 2019 Miserable Bastards, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

print('start')
if __name__ == '__main__':
    print('main')

    cubes = [i*i*i for i in range(10)]
    hundreds = [i*100 for i in range(10)]
    tens = [i*10 for i in range(10)]

    for ii in range(1, 10):
        for jj in range(10):
            for kk in range(10):
#                print("%d %d %d" % (ii, jj, kk))
                cubed = cubes[ii] + cubes[jj] + cubes[kk]
                summed = hundreds[ii] + tens[jj] + kk
                if cubed == summed:
                    print(summed)

print('stop')

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***

