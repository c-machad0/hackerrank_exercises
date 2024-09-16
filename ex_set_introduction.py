def average(array):
    array_modify = set(array)
    avg = sum(array_modify) / len(array_modify)

    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(f'{result:.3f}')