import sys
from pprint import pprint

sys.stdin = open('input5.txt', 'r')

from collections import deque

direction = {
    0: [(0, 0)],
    1: [(-1, 0), (1, 0), (0, 1), (0, -1)],  # 상하좌우
    2: [(-1, 0), (1, 0)],  # 상하
    3: [(0, 1), (0, -1)],  # 좌우
    4: [(-1, 0), (0, 1)],  # 상우
    5: [(1, 0), (0, 1)],  # 하우
    6: [(1, 0), (0, -1)],  # 하좌
    7: [(-1, 0), (0, -1)],  # 상좌
}

def BFS(stx, sty, d):
    q = deque()
    q.append((stx, sty, d))
    visited[stx][sty] = 1
    while q:
        x, y, dp = q.popleft()
        for a, b in direction[board[x][y]]:
            nx = a + x
            ny = b + y
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 0 and not visited[nx][ny] and dp < L:
                if (-a, -b) in direction[board[nx][ny]]:
                    q.append((nx, ny, dp + 1))
                    visited[nx][ny] = 1


for tc in range(1, int(input().rstrip()) + 1):
    N, M, R, C, L = map(int, input().rstrip().split())
    board = [[int(x) for x in input().rstrip().split()] for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    BFS(R, C, 1)
    res = 0
    for v in visited:
        res += sum(v)
    print('#{} {}'.format(tc, res))
