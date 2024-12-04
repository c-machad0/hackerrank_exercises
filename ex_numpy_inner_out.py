import numpy as np

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

numpy_array_a = np.array(array_a)
numpy_array_b = np.array(array_b)

print(np.inner(numpy_array_a,numpy_array_b))
print(np.outer(numpy_array_a,numpy_array_b))


"""
sample input
0 1
2 3

sample output
3
[[0 0]
[2 3]]
"""