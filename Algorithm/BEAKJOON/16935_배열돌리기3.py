import sys
sys.stdin = open('input.txt', 'r')

def one():
    global board
    board = board[::-1]


def two():
    global board
    for i in range(N):
        board[i] = board[i][::-1]


def three():
    global board, N, M
    N, M = M, N
    temp = []
    for x in list(zip(*board)):
        temp.append(list(x)[::-1])
    return temp

def four():
    global board, N, M
    N, M = M, N
    temp = []
    for x in list(zip(*board)):
        temp.insert(0, list(x))
    return temp


def five():
    global board
    temp = [[0]*M for _ in range(N)]
    half_N = N // 2
    half_M = M // 2

    for i in range(half_N):
        for j in range(half_M):
            temp[i][half_M+j] = board[i][j]
    for i in range(half_N):
        for j in range(half_M, M):
            temp[half_N+i][j] = board[i][j]
    for i in range(half_N, N):
        for j in range(half_M, M):
            temp[i][j-half_M] = board[i][j]
    for i in range(half_N, N):
        for j in range(half_M):
            temp[i-half_N][j] = board[i][j]
    return temp

def six():
    global board
    temp = [[0] * M for _ in range(N)]
    half_N = N // 2
    half_M = M // 2

    for i in range(half_N):
        for j in range(half_M):
            temp[half_N+i][j] = board[i][j]
    for i in range(half_N, N):
        for j in range(half_M):
            temp[i][j+half_M] = board[i][j]
    for i in range(half_N, N):
        for j in range(half_M, M):
            temp[i-half_N][j] = board[i][j]
    for i in range(half_N):
        for j in range(half_M, M):
            temp[i][j-half_M] = board[i][j]
    return temp


N, M, R = map(int, input().rstrip().split())
board = [[int(x) for x in input().rstrip().split()] for _ in range(N)]
mode = list(map(int, input().rstrip().split()))
for m in mode:
    if m == 1:
        one()
    elif m == 2:
        two()
    elif m == 3:
        board = three()
    elif m == 4:
        board = four()
    elif m == 5:
        board = five()
    else:
        board = six()

for i in range(N):
    print(*board[i])
