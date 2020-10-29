import sys
sys.stdin = open('input6.txt', 'r')

def cost(x, t):
    global res
    if t > res:
        return
    if x == N:
        if t < res:
            res = t
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            cost(x+1, t+board[x][i])
            visited[i] = False

for tc in range(1, int(input())+1):
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    visited = [False] * N
    res = 987654321
    cost(0, 0)
    print('#{} {}'.format(tc, res))