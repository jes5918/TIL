# 0은 이동 1은벽
# 사방이 막혔을때 super 기회 -1
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        for a, b in delta:
            nx = xx + a
            ny = yy + b
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if flag and arr[nx][ny]:
                continue


N, M = map(int, input().split())
board = [[int(x) for x in input()] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bfs(0, 0)