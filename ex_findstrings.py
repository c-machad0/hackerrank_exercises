def count_substring(string, sub_string):
    count = 0
    start = 0
    
    while True:
        # Tenta encontrar a substring a partir do índice 'start'
        start = string.find(sub_string, start)
        
        # Se find() retornar -1, não há mais ocorrências
        if start == -1:
            break
        
        # Incrementa o contador para cada ocorrência encontrada
        count += 1
        
        # Move o índice 'start' para continuar a busca, permitindo sobreposições
        start += 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
