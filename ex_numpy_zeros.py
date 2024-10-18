import numpy

num = list(map(int, input().split()))

print(numpy.zeros(num, dtype = int)) # 'x' linhas, 'y' colunas, em 'z' vezes
print(numpy.ones(num, dtype = int)) # 'x' linhas, 'y' colunas, em 'z' vezes
"""
sample input
3 3 3

sample output
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
"""