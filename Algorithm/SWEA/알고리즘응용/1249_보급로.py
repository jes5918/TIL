# 출발지에서 도착지까지 거리는 고려하지 않아도 된다 = 깊이에 대해서만 고민
# 출발지는 좌상단 도착지는 우하단 0 으로 표시됨
# 이동은 상하좌우
# 출발지와 도착지를 제외한 0인 곳은 복구작업이 필요 없는곳 = 이런쪽으로 가야함
# 어떻게 문제를 풀어갈까..... 음 BFS
# dist 배열을 활용하여 죄단거리 갱신하는 방법을 사용하자
# deck을 쓰구 디큐한다
import sys
from pprint import pprint
sys.stdin = open('input10.txt', 'r')

from collections import deque
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 우 상 좌

def BFS(x, y):
    global res
    q = deque()
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        for a, b in delta:
            nx = a + xx
            ny = b + yy
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] > dist[xx][yy] + board[nx][ny]:
                    dist[nx][ny] = dist[xx][yy] + board[nx][ny]
                    q.append((nx, ny))


for tc in range(1, int(input().rstrip()) + 1):
    N = int(input().rstrip())
    board = [[int(x) for x in input()] for _ in range(N)]
    dist = [[98765321] * N for _ in range(N)]
    dist[0][0] = 0
    BFS(0, 0)
    print('#{} {}'.format(tc, dist[N - 1][N - 1]))
