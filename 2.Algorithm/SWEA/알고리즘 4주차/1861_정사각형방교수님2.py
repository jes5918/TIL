import sys

sys.stdin = open('1861.txt', 'r')

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    dist = [1] * (N * N + 1)
    num = [0] * (N * N + 1)

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            num[arr[i][j]] = (i, j)

    for i in range(2, N * N + 1):
        for a, b in delta:
            xx = num[i][0] + a
            yy = num[i][1] + b
            if 0 <= xx < N and 0 <= yy < N and i - arr[xx][yy] == 1:
                dist[i] = dist[i - 1] + 1

    ans_num, ans_dist = N * N, 0
    for i in range(1, N*N+1):
        if dist[i] > ans_dist:
            ans_num = i
            ans_dist = dist[i]

    print('#{} {} {}'.format(tc, ans_num-(ans_dist-1), ans_dist))
