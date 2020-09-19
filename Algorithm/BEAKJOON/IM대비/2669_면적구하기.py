board = [[0] * 101 for _ in range(101)]
for _ in range(4):
    st_x, st_y, ed_x, ed_y = map(int, input().split())
    for i in range(st_x, ed_x):
        for j in range(st_y, ed_y):
            if board[i][j] == 0:
                board[i][j] = 1
res = 0
for b in board:
    res += b.count(1)
print(res)
