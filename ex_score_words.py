"""
A pontuação de uma unica palavra é 2 se a palavra conter um numero
par de vogais. Caso contrário, a pontuação sera 1. A pontuação de toda
a lista de palavras é a soma da pontuação de todas as palavras da lista
"""
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = []

    for word in words: # Para cada palavra na lista
        total = 0 # Total é zerado a cada nova palavra em que ele iterar
        for letter in word: # Para cada letra na palavra
            if letter in vowels:
                total = total + 1
        if total % 2 == 0: # Se o total de vogais da palavra for par
            score.append(2)
        else:
            score.append(1)

    print(sum(score))                

n = int(input())

words = list(map(str, input().split()))

score_words(words)

"""
sample input
2
hacker book

sample output
4

Vou ler a string e contar o numero de vogais. Depois, vou saber se
a quantidade de vogais é par ou não
"""