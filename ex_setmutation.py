n = int(input())

set_a = set(map(int, input().split()))

n_sets = int(input())

for _ in range(n_sets):
    op, x = input().split()
    set_b = set(map(int, input().split()))

    if op == 'intersection_update':
        set_a.intersection_update(set_b)
    elif op == 'update':
        set_a.update(set_b)
    elif op == 'symmetric_difference_update':
        set_a.symmetric_difference_update(set_b)
    elif op == 'difference_update':
        set_a.difference_update(set_b)
    else:
        raise ValueError

print(sum(set_a))