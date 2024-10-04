from collections import Counter

string = input()

char_count = Counter(string)

# A contagem (x[1]) é negada para ordenação decrescente.
# O caractere (x[0]) é classificado em ordem crescente (alfabética) como critério de desempate.
sorted_counts = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

# Imprimir os três caracteres mais frequentes (ou menos, se houver menos de 3)
for key, value in sorted_counts[:3]:
    print(f'{key} {value}')

"""
from collections import Counter

# Entrada da string
string = input()

# Contar as ocorrências dos caracteres usando Counter
char_count = Counter(string)

# Obter os três caracteres mais comuns
most_common_three = char_count.most_common(3)

# Imprimir os três caracteres mais frequentes
for key, value in most_common_three:
    print(f'{key} {value}')

"""