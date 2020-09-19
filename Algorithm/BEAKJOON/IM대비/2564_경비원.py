N, M = map(int, input().split())
K = int(input())

arr = [[0] * N]
for _ in range(M-2):
    arr.append([0] + [-1 for _ in range(N-2)] + [0])
arr.append([0] * N)

for _ in range(K):
    a, b = map(int, input().split())
    if a == 1: arr[0][b] = 1
    elif a == 2: arr[M-1][b] = 1
    elif a == 3: arr[b][0] = 1
    else: arr[b][N-1] = 1
px, py = map(int, input().split())

