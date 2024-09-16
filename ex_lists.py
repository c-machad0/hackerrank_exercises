if __name__ == '__main__':
    n = int(input())
    arr = [] # lista onde os numeros serão armazenados
    
    for i in range(n):
        command = input().split() # recebe uma lista de palavras divididas pelo split()

        # command[0] refere-se ao comando desejado
        # command[i] refere-se a proxima string digitada e lida
        if command[0] == 'insert':
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(arr)
        elif command[0] == 'remove':
            arr.remove(int(command[1]))
        elif command[0] == 'append':
            arr.append(int(command[1]))
        elif command[0] == 'sort':
            arr.sort()
        elif command[0] == 'pop':
            arr.pop()
        elif command[0] == 'reverse':
            arr.reverse()