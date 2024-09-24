from itertools import combinations_with_replacement

string, size = input().split()

string = sorted(string.upper())
size = int(size)

for i in combinations_with_replacement(string, size):
    print(*i, sep='')