# You're playing Battleship on a grid of cells with R rows and C columns. There are # 0 or more 
# battleships on the grid, each occupying a single distinct cell. The cell in the 
# ith row from the top and jth column from the left either contains a battleship (G_ij=1) or doesn't (G_ij=0)

# You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly at random 
# from the R∗C possible cells. You're interested in the probability that the cell hit by your shot contains a 
# battleship.

# Sample test case #1
# R = 2
# C = 3
# G = 0 0 1
#     1 0 1
# Expected Return Value = 0.50000000

# Sample test case #2
# R = 2
# C = 2
# G = 1 1
#     1 1
# Expected Return Value = 1.00000000

from typing import List

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  
  a = b = R * C
  
  for i in range(R):
    for j in range(C):
      if G[i][j] == 0:
        a -= 1
  
  return a / b

if __name__ == "__main__":
    assert getHitProbability(2, 3, [ [0, 0, 0], [1, 0, 1] ]) == 0.333333
    # test2()
    print("Everything passed")