def dfs(x):
    visited[x] = 1
    print(x, end=' ')
    for i in range(1, N+1):
        if arr[x][i] and not visited[i]:
            dfs(i)

def bfs(x):
    q = []
    visited = [0] * (N + 1)
    q.append(x)
    visited[x] = 1
    print(x, end=' ')
    while q:
        xx = q.pop(0)
        for nx in range(1, N+1):
            if arr[xx][nx] and not visited[nx]:
                print(nx, end=' ')
                visited[nx] = 1
                q.append(nx)

N, M, V = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    m1, m2 = map(int, input().split())
    arr[m1][m2] = arr[m2][m1] = 1
dfs(V)
print()
bfs(V)
print()

