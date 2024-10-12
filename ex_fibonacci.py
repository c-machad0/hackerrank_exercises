num = int(input())
fib_seq = [0, 1] # São os primeiros numeros da sequencia
if num == 0: # Caso base
    print([])

if num == 1: # Caso base
    print([0])

for i in range(2, num + 1): # Inicia a partir do terceiro numero e vai ate o numero digitado 'num + 1'
    # A soma dos dois numeros anteriores
    # Se i está no indice 3, então fib_seq[3 - 1] + fib_seq[3 - 2]
    # fib_seq[2] + fib_seq[1] = 1 + 1 = 2
    next_value = fib_seq[i - 1] + fib_seq[i - 2]
    fib_seq.append(next_value)

print(fib_seq)