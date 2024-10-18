import numpy

arr = input().split()

my_array = numpy.array(arr, int)

print(numpy.reshape(my_array, (3,3))) # Transforma os dados digitados em uma matriz 3x3

"""
sample input
1 2 3 4 5 6 7 8 9

sample output
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""