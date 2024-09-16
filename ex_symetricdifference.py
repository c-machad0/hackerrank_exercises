n1 = int(input())

set_a = set(map(int, input().split()))

n2 = int(input())

set_b = set(map(int, input().split()))

set_result = set_a ^ set_b

for i in sorted(set_result):
    print(i)