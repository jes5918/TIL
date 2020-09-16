import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(50000)

def dfs(x, y):
    visited[x][y] = True
    for a, b in delta:
        nx = a + x
        ny = b + y
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if visited[nx][ny]:
            continue
        if not field[nx][ny]:
            continue
        dfs(nx, ny)
    return


for tc in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[False] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = True

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)