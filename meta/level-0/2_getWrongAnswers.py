# There's a multiple-choice test with N questions, numbered from 1 to N. Each question has 
# 2 answer options, labelled A and B. You know that the correct answer for the ith question 
# is the ith character in the string C, which is either "A" or "B", but you want to get a score of 
# 0 on this test by answering every question incorrectly.

# Sample test case #1
# N = 3
# C = ABA
# Expected Return Value = BAB

# Sample test case #2
# N = 5
# C = BBBBB
# Expected Return Value = AAAAA

def getWrongAnswers(N: int, C: str) -> str:
  result = ''
  for i in range(N):
    if C[i] == 'A':
      result += 'B' 
    else: 
      result += 'A'
      
  return result