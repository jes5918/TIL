def dfs(x, y):
    global cnt
    visited.append((x, y))
    for a, b in delta:
        nx = a + x
        ny = b + y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if (nx, ny) in visited:
            continue
        if not arr[nx][ny]:
            continue
        dfs(nx, ny)
    cnt += 1

N = int(input())
arr = [[int(x) for x in input()] for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]
visited = []
result = []
count = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if (i, j) not in visited and arr[i][j]:
            count += 1
            dfs(i, j)
            result.append(cnt)
            cnt = 0
print(count)
result.sort()
for i in range(len(result)):
    print(result[i])