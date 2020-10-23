import sys
sys.stdin = open('input.txt', 'r')

def DFS(x):
    global temp_sum, result
    if temp_sum > result:
        return
    else:
        visited[x] = True
    if False in visited:
        for i in range(N):
            if visited[i] == False:
                temp_sum += board[x][i]
                DFS(i)
                temp_sum -= board[x][i]
    else:
        temp_sum += board[x][0]
        if temp_sum < result:
            result = temp_sum
        temp_sum -= board[x][0]
    visited[x] = False

for tc in range(1, int(input())+1):
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    temp_sum = 0
    result = 987654321
    visited = [False] * N
    DFS(0)
    print('#{} {}'.format(tc, result))

