n = int(input())

num = list(map(int, input().split()))

num = set(num[::-1])
    
n_command = int(input())

for i in range(n_command):
    command = input().split()

    if command[0] == 'pop':
        try:
            num.pop()
        except:
            None
    elif command[0] == 'remove':
        try:
            num.remove(int(command[1]))
        except:
            None
    elif command[0] == 'discard':
        num.discard(int(command[1]))

print(sum(num))