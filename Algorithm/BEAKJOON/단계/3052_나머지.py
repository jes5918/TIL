res = []
for _ in range(10):
    N = int(input())
    temp = N % 42
    res.append(temp)
res = list(set(res))
print(len(res))