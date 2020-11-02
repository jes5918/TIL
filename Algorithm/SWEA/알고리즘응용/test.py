# 시험문제 예상
# 전체 큰 행렬을 하나주고 부분을 나눠서
# 부분부분 돌리는 행렬
# mode에 따라서 돌린다

import sys
from pprint import pprint
sys.stdin = open('input2.txt', 'r')

def rotate90(arr, m, x, y):
    temp = [[0] * m for _ in range(m)]
    for xx in range(m):
        for yy in range(m):
            temp[yy][m-xx-1] = arr[xx+x][yy+y]
    return temp


def rotate180(arr, m, x, y):
    temp = [[0] * m for _ in range(m)]
    for xx in range(m):
        for yy in range(m):
            temp[m-xx-1][m-yy-1] = arr[xx+x][yy+y]
    return temp


def rotate270(arr, m, x, y):
    temp = [[0] * m for _ in range(m)]
    for xx in range(m):
        for yy in range(m):
            temp[m-yy-1][xx] = arr[xx+x][yy+y]
    return temp


def inserting(a, m, x, y):
    for xx in range(m):
        for yy in range(m):
            board[x+xx][y+yy] = a[xx][yy]
    return


N, M = 6, 3
direction = [(450, 1, 3), (540, 2, 2), (270, 3, 3)]
board = [[int(x) for x in input().split()] for _ in range(N)]
for x, r, c in direction:
    if x % 360 == 90:
        ro90 = rotate90(board, M, r, c)
        inserting(ro90, M, r, c)
    elif x % 360 == 180:
        ro180 = rotate180(board, M, r, c)
        inserting(ro180, M, r, c)
    elif x % 360 == 270:
        ro270 = rotate270(board, M, r, c)
        inserting(ro270, M, r, c)
    else:
        continue
