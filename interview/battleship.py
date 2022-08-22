from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  total_cells = R*C
  
  if total_cells < 1:
    return 0.0
  
  total_ships = 0
    
  for yy in range(R):
    for xx in range(C):
      if G[yy][xx] > 0:
        total_ships += 1

  return total_ships/total_cells

if __name__ == '__main__':
  r = 2
  c = 3
  g = [[0, 0, 1], [1, 0, 1]]
  result = getHitProbability(r, c, g)
  print(f"result {result}")

  r = 2
  c = 2
  g = [[1, 1], [1, 1]]
  result = getHitProbability(r, c, g)
  print(f"result {result}")