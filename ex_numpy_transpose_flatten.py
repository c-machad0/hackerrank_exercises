import numpy

row, columns = map(int, input().split())

my_array = []

for i in range(row): # Itera sobre a quantidade de linhas
    num = list(map(int, input().split())) # Variavel que recebe os numeros digitados e transforma diretamente em uma lista
    my_array.append(num) # Adiciona nao variavel 'my_array'

change_array = numpy.array(my_array) # Transforma a lista em um array numpy
print(numpy.transpose(change_array)) # Transforma em uma matriz transposta
print(change_array.flatten()) # Transforma a matriz em matriz unidimensional
"""
sample input
2 2
1 2
3 4

sample output
[[1 3]
 [2 4]]
[1 2 3 4]
"""