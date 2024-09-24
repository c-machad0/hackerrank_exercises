from itertools import product
# product - calcula o produto cartesiano de iteraveis de entrada
# product(a, b) = ((x, y) for x in A for y in B)

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = list(product(a, b))
print(*result)