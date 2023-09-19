# A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right.
#  Social distancing guidelines require that every diner be seated such that 
# K seats to their left and K seats to their right (or all the remaining seats to that 
# side if there are fewer than K) remain empty.

# There are currently M diners seated at the table, the ith of whom is in seat Si.
# No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.

# Determine the maximum number of additional diners who can potentially sit at the table 
# without social distancing guidelines being violated for any new or existing diners, 
# assuming that the existing diners cannot move and that the additional diners will 
# cooperate to maximize how many of them can sit down.

# Sample test case #1
# N = 10
# K = 1
# M = 2
# S = [2, 6]
# Expected Return Value = 3
# In the first case, the cafeteria table has N=10 seats, with two diners currently at seats 
# 2 and 6 respectively. The table initially looks as follows, with brackets covering the 
# K = 1 seat to the left and right of each existing diner that may not be taken.
#  1 2 3 4 5 6 7 8 9 10
#  [   ]   [   ]
# Three additional diners may sit at seats 4, 8 and 10 without violating the social distancing guidelines.

# Sample test case #2
# N = 15
# K = 2
# M = 3
# S = [11, 6, 14]
# Expected Return Value = 1
# In the second case, only 1 additional diner is able to join the table, by sitting in any of the first 
# 3 seats.

from typing import List
import math

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:

  S.sort()
  
  res = 0
  for i in range(M-1):
    j = i+1
    free_spacing = S[j] - S[i] - 1
    num_dinners = math.floor( (free_spacing - K)/(K+1) )
    if num_dinners > 0: 
      res += num_dinners

  for i in range(0,2):
    print(i)
    
  free_spacing_initial = S[0] - 1
  num_dinners_initial = math.floor( free_spacing_initial/(K+1) )
  if num_dinners_initial > 0: 
      res += num_dinners_initial
  
  free_spacing_final = N - S[M-1] 
  num_dinners_final = math.floor( free_spacing_final/(K+1) )
  if num_dinners_final > 0: 
    res += num_dinners_final
  
  return res


getMaxAdditionalDinersCount(10, 1, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# ===== IMPORTANTE =====
# ORDENAR LISTAS QDO NÃO TIVEREM ORDENADAS: S.sort()
# LEMBRAR math.floor E math.ceil
# QUANDO PRECISAR ITERAR SOBRE 2 PARAMETROS FAZER UM FOR COM i NORMAL ATÉ range(n-1) E DEPOIS j = i+1

# ===== SOLUCAO =====
# CONTAR QUANTOS ESPAÇOS LIVRES EXISTEM ENTRE PESSOAS
# TC 1
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     X           X
# entre 2 e 6 existem 3 espaços livres: free_spacing = S[j] - S[i] - 1   
# contar quantas pessoas cabem ai... fazer chinês para descobrir a fórmula: floor( free_spacing-K / (K+1) ) 
# observar que no início e no fim, i.e., qdo nao existe uma pessoa, a formula muda 
  
# DRAFT
# para descobrir formula entre pessoas 
#   k=2                          k=1
#  14: 4  f( space-k / (k+1) )   11: 5 => f( space-k / (k+1) ) 
#  11: 3                         9: 4
#   8: 2                         7: 3
#   5: 1                         5: 2
 
# para descobrir formula entre pessoas no início, i.e., de 0 a S[0] e no fim, i.e., S[M-1] a N+1
#   k=3
#   12:3
#   8: 2
#   4: 1
  
#   k=2
#   9: 3
#   6: 2        
#   3: 1
  
#   k=1
#   6: 3
#   4: 2
#   2: 1