import sys

for _ in range(4):
    st1x, st1y, ed1x, ed1y, st2x, st2y, ed2x, ed2y = map(int, sys.stdin.readline().split())
    N = max(st1x, st1y, ed1x, ed1y, st2x, st2y, ed2x, ed2y)
    board = [[False] * (N + 1) for _ in range(N + 1)]
    for i in range(st1x, ed1x):
        for j in range(st1y, ed1y):
            board[i][j] += 1
    for x in range(st2x, ed2x):
        for y in range(st2y, ed2y):
            board[x][y] += 1

    temp = []
    for b in board:
        if b.count(2):
            temp.append(b.count(2))
    print(temp)