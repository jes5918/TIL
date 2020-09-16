import sys
sys.setrecursionlimit(50000)

def bfs():
    q = [[0, 0]]
    visited[0][0] = 1
    while q:
        x, y = q.pop(0)
        for a, b in delta:
            nx = x + a
            ny = y + b
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

N, M = map(int, input().split())
board = [[int(x) for x in input()] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited[0][0] = 1
bfs()
print(visited[N-1][M-1])
