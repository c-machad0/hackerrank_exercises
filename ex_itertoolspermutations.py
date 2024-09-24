from itertools import permutations

string, size = input().split()

permutation = sorted(list(permutations(string.upper(), int(size))))

for p in permutation:
    print(*p, sep='')

