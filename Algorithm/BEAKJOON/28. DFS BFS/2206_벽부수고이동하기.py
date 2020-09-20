<<<<<<< HEAD
=======
# 0은 이동 1은벽
# 사방이 막혔을때 super 기회 -1
>>>>>>> f6b4de17086c8cf1e0d3b8f10035cbcf6fd1f5f4
from collections import deque

def bfs(x, y):
    q = deque()
<<<<<<< HEAD
    q.append((x, y, True, 1))
    while q:
        xx, yy, flag, cnt = q.popleft()
        if (xx, yy) == (N-1, M-1):
            res.append(cnt)
            continue
        for a, b in delta:
            nx = a + xx
            ny = b + yy
=======
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        for a, b in delta:
            nx = xx + a
            ny = yy + b
>>>>>>> f6b4de17086c8cf1e0d3b8f10035cbcf6fd1f5f4
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
<<<<<<< HEAD
            if board[nx][ny]:
                if flag:
                    q.append((nx, ny, False, cnt + 1))
                    visited[nx][ny] = 1
                    continue
                else:
                    continue
            q.append((nx, ny, flag, cnt + 1))
            visited[nx][ny] = 1
=======
            if flag and arr[nx][ny]:
                continue
>>>>>>> f6b4de17086c8cf1e0d3b8f10035cbcf6fd1f5f4


N, M = map(int, input().split())
board = [[int(x) for x in input()] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
<<<<<<< HEAD
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = []
bfs(0, 0)
print(res)
if res:
    print(min(res))
else:
    print('-1')
=======
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bfs(0, 0)
>>>>>>> f6b4de17086c8cf1e0d3b8f10035cbcf6fd1f5f4
