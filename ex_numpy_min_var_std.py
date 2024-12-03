import numpy

row, column = map(int, input().split()) # Define o tamanho da matriz linhas x colunas
my_arr = [] # Array que receberá os valores da matriz

for i in range(row): # Laço que itera sobre a quantidade de linhas
    num = list(map(float, input().split())) # Variavel que recebe os numeros de cada linha, no tipo float e transforma em list
    my_arr.append(num) # Adiciona cada linha da lista 'num', na lista 'my_array'

np_array = numpy.array(my_arr) # Variavel que recebe a lista antiga como um array numpy

print(numpy.mean(np_array, axis=1)) # Imprime a media do array, por colunas
print(numpy.var(np_array, axis=0)) # Imprime a variancia do array, por linhas
print(round(numpy.std(np_array, axis=None), 11)) # Imprime o desvio padrão do array de todos os elementos

"""
sample input
2 2
1 2
3 4

sample output
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
"""

"""
Calculos matemáticos
- mean (média) -> μ = 1 + 2/2 = 1.5
Soma todos os elementos e divide pela quantidade de elementos do conjunto

- var (variância)
Conjunto de dados: [2, 4, 6, 8]
1.Calcula a média
2 + 4 + 6 + 8 / 4 = 5

2. Subtrai a média de cada elemento
2 - 5 = -3
4 - 5 = -1
6 - 5 = 1
8 - 5 = 3

3. Eleve cada diferença ao quadrado
(-3)² = 9
(-1)² = 1
(1)² = 1
(3)² = 9

4. Some os quadrados
9 + 1 + 1 + 9 = 20

5. Divida pela quantidade de elementos da população (n)
var = 20 / 4 = 5

6. Se for uma amostra, divida n(numero de elementos) - 1
var = 20 / 4-1 = 20/3 ≈ 6.67

- std (desvio padrão)
1.Calcula a média
2. Calcule a variância
3. O desvio padrão é a raiz quadrada da variância
var = 5 (população)
var ≈ 6.67 (amostra)

std = √5 ≈ 2.582 (população)
std = √6.67 ≈ 2.582 (amostra)
"""