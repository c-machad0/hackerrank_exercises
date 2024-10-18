import numpy

row1, row2, columns = map(int, input().split())
my_array = []

for i in range(row1 + row2):
    num = list(map(int, input().split()))
    my_array.append(num)

change_array = numpy.array(my_array)
print(change_array)
"""
sample input
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4

sample output
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
"""