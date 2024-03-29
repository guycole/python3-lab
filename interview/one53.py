#
# Title:one53.py
# Description: 153 in python
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

