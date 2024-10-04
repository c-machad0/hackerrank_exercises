n, s = (input()).split()

res=[]

for _ in range(int(s)):
    x = list(map(float, input().split()))
    res.append(x)

t = (list(zip(*res)))

for i in t:
    print(sum(i)/float(s))