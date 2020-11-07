import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint
from collections import deque
from copy import deepcopy

delta = [(1,0), (0, 1),(-1, 0),(0,-1)]

def BFS(virus, copy_arr):
    q = deque()
    temp = 0
    for a, b in virus:
        q.append((a, b))
    while q:
        x, y = q.popleft()
        for a, b in delta:
            nx = a + x
            ny = b + y
            if 0 <= nx < N and 0 <= ny < M and copy_arr[nx][ny] == 0:
                copy_arr[nx][ny] = 2
                temp += 1
                q.append((nx,ny))
    return safa_area - temp - 3


def check(start, cnt):
    global result
    if cnt == 3:
        arr = deepcopy(board)
        temp = BFS(virus, arr)
        result = max(temp, result)
        return
    for i in range(start, N * M):
        x = i // M
        y = i % M
        if board[x][y] == 0:
            board[x][y] == 1
            check(i+1, cnt+1)
            board[x][y] == 0


N, M = map(int, sys.stdin.readline().rstrip().split())
board = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
virus = []
path = []
result = 0
safa_area = 0
for i in range(N):
    for j in range(M):
        t = board[i][j]
        if t == 2:
            virus += [(i, j)]
        elif t == 0:
            safa_area += 1
check(0, 0)
print(result)