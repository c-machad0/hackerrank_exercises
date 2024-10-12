cube = lambda x: x**3 # Função lambda para calcular o cubo em cada elemento da lista

def fibonacci(n):
    fibo = [0, 1] # Inicializa a lista com os dois primeiros numeros
    if n == 0:
        return [] # Sequencia de fibonacci com nenhum termo é uma lista vazia
    
    if n == 1:
        return [0] # Sequencia de fibonacci com apenas um termo é 0
    
    for i in range(2, n): # Inicia a iteração a partir do indice 2
        next_value = fibo[i - 1] + fibo[i - 2]
        fibo.append(next_value)
    
    return fibo

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

"""
sample input
5

sample output
[0, 1, 1, 8, 27]
"""