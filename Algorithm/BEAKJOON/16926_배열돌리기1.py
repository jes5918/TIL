import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')


#
# delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
# def rotate():
#     global board, temp
#     for k in range(min(N, M) // 2):
#         temp2 = []
#         r, c, direction, num = k, k, 0, 0
#         while True:
#             if num >= 2 * (N + M - (4 * k)) - 4:
#                 break
#             if direction == 4:
#                 break
#             x, y = r, c
#             nr = r + delta[direction][0]
#             nc = c + delta[direction][1]
#             if k <= nr < N-k and k <= nc < M-k:
#                 r, c = nr, nc
#                 temp[x][y] = board[nr][nc]
#                 temp2.append(board[nr][nc])
#                 num += 1
#             else:
#                 direction += 1
#
# N, M, R = map(int, input().rstrip().split())
# board = [[int(x) for x in input().rstrip().split()] for _ in range(N)]
# for _ in range(R):
#     temp = [[0] * M for _ in range(N)]
#     rotate()
#     board = temp
# for b in board:
#     print(*b)


# def rotate():
#     num = 0
#     temp = [[0] * M for _ in range(N)]
#
#     while min(N, M) // 2 > num:
#         for i in range(num, N - num):
#             for j in range(num, M - num):
#                 if j == num and i != N - num - 1:
#                     temp[i + 1][j] = arr[i][j]
#                 elif i == N - num - 1 and j != M - num - 1:
#                     temp[i][j + 1] = arr[i][j]
#                 elif j == M - num - 1 and i != num:
#                     temp[i - 1][j] = arr[i][j]
#                 elif i == num and j != num:
#                     temp[i][j - 1] = arr[i][j]
#         num += 1
#     return temp
#
#
# N, M, R = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# for _ in range(R):
#     arr = rotate()
#
# for a in arr:
#     print(*a)

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def rotate(p, ll, rl, ul, dl):
    i, j = p, p
    direction = 0
    while True:
        i = i + delta[direction][0]
        j = j + delta[direction][1]
        if i == ul or i == dl or j == ll or j == rl:
            i = i - delta[direction][0]
            j = j - delta[direction][1]
            direction += 1
            i = i + delta[direction][0]
            j = j + delta[direction][1]
        if i == p and j == p:
            return
        board[p][p], board[i][j] = board[i][j], board[p][p]

N, M, R = map(int, input().rstrip().split())
board = [[int(x) for x in input().rstrip().split()] for _ in range(N)]
for k in range(min(N, M)//2):
    for _ in range(R % (2 * (N + M - (4 * k) - 4))):
        rotate(k, k-1, M-k, k-1, N-k)
for b in board:
    print(*b)