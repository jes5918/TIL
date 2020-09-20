from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y, True, 1))
    while q:
        xx, yy, flag, cnt = q.popleft()
        if (xx, yy) == (N-1, M-1):
            res.append(cnt)
            continue
        for a, b in delta:
            nx = a + xx
            ny = b + yy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny]:
                if flag:
                    q.append((nx, ny, False, cnt + 1))
                    visited[nx][ny] = 1
                    continue
                else:
                    continue
            q.append((nx, ny, flag, cnt + 1))
            visited[nx][ny] = 1


N, M = map(int, input().split())
board = [[int(x) for x in input()] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = []
bfs(0, 0)
print(res)
if res:
    print(min(res))
else:
    print('-1')