import sys
sys.stdin = open('input3.txt', 'r')

N, M, R = map(int, input().split()) # 행렬의 크기
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 우 상 좌
board = [[int(x) for x in input().split()] for _ in range(N)]
result = [[0] * M for _ in range(N)]
direction, row, col = 0, 0, 0
num = 1

while num <= N * M:
    temp = board[row][col]
    num += 1
    new_row = row + delta[direction][0]
    new_col = col + delta[direction][1]
    if result[row][col] != 0:
        row += 1
        col += 1
        direction = 0
        num -= 1
    if 0 <= new_row < N and 0 <= new_col < M:
        if result[row][col] != 0:
            row = new_row + 1
            col = new_col + 1
            direction = 0
            num -= 1
            continue
        row, col = new_row, new_col
    else:
        direction = (direction + 1) % 4
        continue
    result[row][col] = temp

for i in range(N):
    print(*result[i])