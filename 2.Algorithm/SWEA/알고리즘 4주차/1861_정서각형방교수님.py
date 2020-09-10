import sys
sys.stdin = open('1861.txt', 'r')

def bfs(x, y):
    global ans_num, ans_dist
    q = [(x, y)]
    cnt = 0

    while q:
        xx, yy = q.pop(0)
        cnt += 1
        for a, b in delta:
            nx = a + xx
            ny = b + yy

            if arr[nx][ny] - arr[xx][yy] == 1:
                q.append((nx, ny))

    if cnt >= ans_dist:
        if cnt == ans_dist:
            ans_num = min(ans_num, arr[x][y])
        else:
            ans_num = arr[x][y]

        ans_dist = cnt

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * (N+2) for _ in range(N+2)]

    for i in range(1, N+1):
        tmp = list(map(int, input().split()))
        for j in range(1, N+1):
            arr[i][j] = tmp[j-1]

    ans_dist = 0
    ans_num = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            bfs(i, j)

    print('#{} {} {}'.format(tc, ans_num, ans_dist))