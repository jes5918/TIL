import sys

sys.stdin = open('input.txt', 'r')

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def findstart():
    global start
    max_road = 0
    for i in range(N):
        for j in range(N):
            if max_road < board[i][j]:
                max_road = board[i][j]
                start = [(i, j)]
            elif max_road == board[i][j]:
                start.append((i, j))


def DFS(x, y, chance, dp):
    global res
    res = max(res, dp)
    for aa, bb in delta:
        nx = aa + x
        ny = bb + y
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if not chance:
                if board[x][y] > board[nx][ny]:
                    visited[nx][ny] = True
                    DFS(nx, ny, False, dp + 1)
                    visited[nx][ny] = False
            else:
                if board[x][y] > board[nx][ny]:
                    visited[nx][ny] = True
                    DFS(nx, ny, True, dp + 1)
                    visited[nx][ny] = False
                for i in range(1, K + 1):
                    if board[x][y] > board[nx][ny] - i:
                        board[nx][ny] -= i
                        visited[nx][ny] = True
                        DFS(nx, ny, False, dp + 1)
                        visited[nx][ny] = False
                        board[nx][ny] += i


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    start = []
    findstart()
    result = 0
    for a, b in start:
        res = 0
        visited = [[False] * N for _ in range(N)]
        visited[a][b] = True
        DFS(a, b, True, 1)
        result = max(res, result)
    print('#{} {}'.format(tc, result))