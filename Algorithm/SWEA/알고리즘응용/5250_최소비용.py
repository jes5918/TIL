import sys
sys.stdin = open('input8.txt', 'r')

from collections import deque
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dijkstra(board):
    visited = [[False] * N for _ in range(N)]
    dist = [[98765321] * N for _ in range(N)]
    dist[0][0] = 0
    check = set()
    check.add((0, 0))
    while True:
        minval = float('inf')
        for xx, yy in check:
            if dist[xx][yy] < minval and not visited[xx][yy]:
                minval = dist[xx][yy]
                x, y = xx, yy

        visited[x][y] = True
        check.remove((x, y))

        if x == N - 1 and y == N - 1:
            return dist

        for a, b in delta:
            nx = a + x
            ny = b + y
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[nx][ny] > board[x][y]:
                    temp = board[nx][ny] - board[x][y] + 1
                else:
                    temp = 1

                if dist[nx][ny] > dist[x][y] + temp:
                    dist[nx][ny] = dist[x][y] + temp
                    check.add((nx, ny))


def BFS(x, y):
    dist = [[98765321] * N for _ in range(N)]
    dist[0][0] = 0
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
    return dist


for tc in range(1, int(input().rstrip()) + 1):
    N = int(input().rstrip())
    board = [[int(x) for x in input().rstrip().split()] for _ in range(N)]
    # 다익스트라 origin => 실행시간 0.15724s
    dist = dijkstra(board)
    # # BFS 변형 다익스트라 => 실행시간 0.21522s
    # dist = BFS(0, 0)
    print('#{} {}'.format(tc, dist[N - 1][N - 1]))
