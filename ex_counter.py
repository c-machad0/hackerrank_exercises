from collections import Counter

k = int(input())

room = list(map(int, input().split()))

# A função Counter retorna a quantidade de vezes que um item da lista ocorre,
# por meio de chave, valor
for index, count in Counter(room).items():
    # index = chave e count = valor
    if count == 1:
        print(index)
        break

"""
list1 = list(map(int, input().split()))
set1 = set(list1)

for x in set1:
    try:
        list1.remove(x)
        list1.remove(x)
    except Exception:
        print(x)
        break
"""