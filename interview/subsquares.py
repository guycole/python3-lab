#
# Title: subsquares.py
# Description: given a large square, test if array of smaller squares can be cut
#
# 0 | 0 | 0
# 0 | 0 | 0
# 0 | 0 | 0
#

def dumper(matmat):
    """ write matrix to stdout """
    for row in range(len(matmat)):
        for col in range(len(matmat[0])):    
            print(matmat[row][col], end=" ")
        print()

def size_match(size, matmat, row, col):
  """ return true if square can be discovered """
  print(f"size match {size} {row} {col}")

  if row+size > len(matmat):
    print("exceed row")
    return False

  if col+size > len(matmat[row]):
    print("exceed col")
    return False
 
  if matmat[row+size-1][col+size-1] == 0:
    for row_ndx in range(size):
      for col_ndx in range(size):
        print(f"mark {row+row_ndx} {col+col_ndx}")
        matmat[row+row_ndx][col+col_ndx] = 1

    return True
 
  return False

def find_square(size, matmat):
  """ find a vacant space in the matrix """
  print(f"find square: {size}")

  for row in range(len(matmat)):
    for col in range(len(matmat[row])):
      if matmat[row][col] == 0:
        # vacant space
        if size_match(size, matmat, row, col):
          print("size match true")
          return True

  print("no square size match")
  return False

def square(row, col, squares):
  matmat = []
 
  for row_ndx in range(row):
    matmat.append([0] * col)
  
#  print(f"square len {len(squares)} {squares}")

  for size in squares:
    result = find_square(size, matmat) 
    dumper(matmat)
    if result is False:
      return False

  return True

if __name__ == '__main__':
    print("main")

    print(square(4, 4, [1, 1, 2]))
    print(square(4, 4, [2, 2]))
    print(square(4, 4, [2, 2, 2]))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
