import numpy

row, column = map(int, input().split()) # Variaves que definem o tamanho da matriz row x column (linha x coluna)
my_array = [] # Lista que receberá os numeros

for _ in range (row): # Laço que itera sobre a quantidade de linhas da matriz
    numbers = list(map(int, input().split())) # Variavel que recebe os numeros separados por espaço e transforma em lista
    my_array.append(numbers) # Adiciona cada lista da iteração à lista 'my_array'

array_numpy = numpy.array(my_array) # Transforma 'my_array' em um array numpy
result_sum = numpy.sum(array_numpy, axis=0) # Variavel que recebe a sum do array, por colunas 'axis=0'
print(numpy.prod(result_sum)) # Imprime o produto do resultado da soma do array anterior

"""
sample input
2 2
1 2
3 4

sample output
24
"""