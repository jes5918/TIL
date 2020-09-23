import sys

M, N = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
row = [0]
col = [0]
res = []
for _ in range(K):
    method, num = map(int, sys.stdin.readline().split())
    if method:
        col.append(num)
    else:
        row.append(num)
col.append(M)
row.append(N)
col.sort()
row.sort()
for i in range(1, len(row)):
    for j in range(1, len(col)):
        res.append((row[i]-row[i-1])*(col[j]-col[j-1]))
print(max(res))
