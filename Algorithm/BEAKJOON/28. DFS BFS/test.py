from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y, True))
    while q:
        xx, yy, ff = q.popleft()
        # if (xx, yy) == (N-1, M-1):
        #     return
        for a, b in delta:
            nx = a + xx
            ny = b + yy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny]:
                if ff:
                    q.append((nx, ny, False))
                    visited[nx][ny] = visited[xx][yy] + 1
                    continue
                else:
                    continue
            q.append((nx, ny, ff))
            visited[nx][ny] = visited[xx][yy] + 1


N, M = map(int, input().split())
board = [[int(x) for x in input()] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
bfs(0, 0)
if visited[N-1][M-1]:
    print(visited[N-1][M-1])
else:
    print('-1')