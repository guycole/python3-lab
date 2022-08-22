# A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right.
# Social distancing guidelines require that every diner be seated such that K seats to their 
# left and K seats to their right (or all the remaining seats to that side if there are fewer 
# than K) remain empty.
# There are currently M diners seated at the table, the iih of whom is in seat Si.
# No two diners are sitting in the same seat, and the social distancing guidelines are
# satisfied.
# Determine the maximum number of additional diners who can potentially sit at the table 
# without social distancing guidelines being violated for any new or existing diners, 
# assuming that the existing diners cannot move and that the additional diners will 
# cooperate to maximize how many of them can sit down.
#
from typing import List

def getMaxAdditionalDinersCount1(N: int, K: int, M: int, S: List[int]) -> int:
  mask = ['v'] * N # vacant

  # populate mask array with diners and buffers
  for ndx1 in S:
    corrected = ndx1-1
    start = corrected-K
    stop = corrected+K+1
    if stop > N:
       stop = N
    for ndx2 in range(start, stop):
      mask[ndx2] = 'b' # buffer
    mask[corrected] = 'd' # diner

  print(mask)

  # discover any available space for diners
  counter = 0
  for ndx1 in range(N):
    if mask[ndx1] == 'v': # process only vacant cell
      start = ndx1-K
      stop = ndx1+K+1
      if stop > N:
        stop = N
      flag = False
      for ndx2 in range(start, stop):
        if mask[ndx2] in ['d', 't']:
          flag = True
      if not flag:
        mask[ndx1] = 't'
        counter += 1
  
  print(mask)
  
  return counter

if __name__ == '__main__':
  print("begin")
  
  n=10
  k=1
  m=2
  s=[2, 6]
  result = getMaxAdditionalDinersCount1(n, k, m, s)
  print(f"result:{result}")

  n=15
  k=2
  m=3
  s=[11, 6, 14]

  result = getMaxAdditionalDinersCount1(n, k, m, s)
  print(f"result:{result}")

  print("end")
