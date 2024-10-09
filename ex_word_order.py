from collections import Counter

num = int(input())

words = []
for _ in range(num):
    word = input()
    words.append(word)

# Armazena em uma lista, o tamanho de cada palavra na lista 'words'
size_words = [len(char) for char in words]

# sum(size_words) soma os valores de cada indice da lista
# Valores que representam os tamanhos de cada palavra 
if sum(size_words) < 10**6:
    word_counts = Counter(words)

    total = len(word_counts) # Armazena a quantidade de palavras contadas (e unicas)
    print(total) 

    for i in Counter(words).values():
        print(i, end=" ")
else:
    print(None)

"""
sample input
4
bcdef
abcdefg
bcde
bcdef

sample output
3
2 1 1
"""