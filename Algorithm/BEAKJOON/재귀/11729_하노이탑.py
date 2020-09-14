def hanoitop(n, a, b, c):
    if n == 1:
        res.append([a, c])
    else:
        hanoitop(n - 1, a, c, b)
        res.append([a, c])
        hanoitop(n - 1, b, a, c)


N = int(input())
res = []
hanoitop(N, 1, 2, 3)
print(len(res))
for i in range(len(res)):
    print(*res[i])
