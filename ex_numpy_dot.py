import numpy

row = int(input()) # Recebe a quantidade de linhas da matriz

array_a = [] # Lista da matriz A
array_b = [] # Lista da matriz B

for _ in range(row): # Laço que itera sobre a quantidade de linhas
    num_a = list(map(int, input().split()))
    array_a.append(num_a)

for _ in range(row):
    num_b = list(map(int, input().split()))
    array_b.append(num_b)

a = numpy.array(array_a) # Transformando a matriz A em array numpy
b = numpy.array(array_b) # Transformando a matriz B em array numpy

print(numpy.dot(a,b)) # Fazendo o produto escalar de matriz

"""
sample input
2
1 2
3 4
1 2
3 4

sample output
[[ 7 10]
[15 22]]
"""
"""
dot - Produto escalar
Linhas da primeira matrix * Colunas da segunda matriz
O numero de colunas da segunda matriz deve ser igual ao numero de linhas da primeira matriz

cross - Produto vetorial
É uma operação definida para dois vetores tridimensionais (vetores com 3 componentes)
u = [u1]    v = [v1]
    [u2]        [v2]
    [u3]        [v3]

w = [u2*v3 - u3*v2]
    [u3*v1 - u1*v3]
    [u1*v2 - u2*v1]
"""