import numpy

def arrays(arr):
    x = numpy.array(arr, float) # Transforma a entrada em dados numpy com o tipo float

    y = numpy.flip(x) # Faz a reversão de um array numpy

    return y

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

"""
sample input
1 2 3 4 -8 -10

sample output
[-10.  -8.   4.   3.   2.   1.]
"""