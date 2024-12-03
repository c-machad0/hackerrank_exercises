import numpy

row, column = map(int, input().split()) # Dimensão da matriz em linhas x colunas
my_arr = [] # Array que receberá os numeros

for i in range(row): # Laço que itera sobre a quantidade de linhas da matriz
    num = list(map(int, input().split())) # Variavel num recebe os numeros por linha e transforma em list
    my_arr.append(num) # Adiciona cada linha à matriz

np_array = numpy.array(my_arr) # Transforma a lista 'my_arr' em um array numpy

result_min = numpy.min(np_array, axis=1) # Calcula o menor valor por linha (axis=1) e retorna um novo array numpy
print(numpy.max(result_min)) # Imprime o maior valor dentre os menores

"""
sample input
4 2
2 5
3 7
1 3
4 0

sample output
3
"""