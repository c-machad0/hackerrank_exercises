number = int(input())

num = list(input().split())

print(all(int(i) >= 0 for i in num) and any([n[::-1] == n for n in num]))
