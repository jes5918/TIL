import sys
sys.stdin = open("input2.txt", "r")

def findmaze(st_x, st_y):
    global result
    if arr[st_x][st_y] == 3:
        result = 1
        return
    visited.append((st_x, st_y))
    for a, b in delta:
        new_X = st_x + a
        new_Y = st_y + b
        if 0 <= new_X < N and 0 <= new_Y < N and (arr[new_X][new_Y] == 0 or arr[new_X][new_Y] == 3) and (new_X, new_Y) not in visited:
            findmaze(new_X, new_Y)

for tc in range(1, int(input())+1):
    N = int(input())
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    arr = [[int(x) for x in input()] for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if arr[i][j] == 2:
                start_x, start_y = i, j
    result = 0
    visited = []
    findmaze(start_x, start_y)
    print('#{} {}'.format(tc, result))

