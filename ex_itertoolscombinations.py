from itertools import combinations

string, size = input().split()

string = sorted(string.upper())
size = int(size)

for i in range(1, size + 1):
    for combination in combinations(string, i):
        print(*combination, sep='')