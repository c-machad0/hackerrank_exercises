from collections import Counter

# Quantidade de sapatos disponíveis
size_list = int(input())

# Lista de sapatos e contagem de cada tamanho
list_of_shoes = Counter(map(int, input().split()))

# Número de clientes
num_customers = int(input())

# Total das vendas
total = 0

# Processar cada cliente
for _ in range(num_customers):
    # Tamanho do sapato desejado e preço oferecido pelo cliente
    shoe, price = map(int, input().split())
    
    # Verificar se há o tamanho disponível
    if list_of_shoes[shoe] > 0:
        # Adicionar o preço ao total
        total += price
        # Reduzir o estoque do sapato vendido
        list_of_shoes[shoe] -= 1

# Mostrar o total arrecadado
print(total)
