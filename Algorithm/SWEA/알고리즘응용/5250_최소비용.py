import sys
from pprint import pprint

sys.stdin = open('input8.txt', 'r')

from collections import deque

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def BFS(x, y):
    q = deque()
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        for a, b in delta:
            nx = a + xx
            ny = b + yy
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] > board[xx][yy]:
                    temp = board[nx][ny] - board[xx][yy] + 1
                else:
                    temp = 1
                if dist[nx][ny] > dist[xx][yy] + temp:
                    dist[nx][ny] = dist[xx][yy] + temp
                    q.append((nx, ny))


for tc in range(1, int(input().rstrip()) + 1):
    N = int(input().rstrip())
    board = [[int(x) for x in input().rstrip().split()] for _ in range(N)]
    dist = [[98765321] * N for _ in range(N)]
    dist[0][0] = 0
    BFS(0, 0)
    print('#{} {}'.format(tc, dist[N - 1][N - 1]))
