for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    min_flag = N * M
    cnt = [0]*3
    cnt[0] = 0
    for x in range(0, N - 2):
        for y in range(0, M):
            if flag[x][y] != 'W':
                cnt[0] += 1
        cnt[1] = 0
        for xx in range(x + 1, N - 1):
            for yy in range(0, M):
                if flag[xx][yy] != 'B':
                    cnt[1] += 1
            cnt[2] = 0
            for xxx in range(xx + 1, N):
                for yyy in range(0, M):
                    if flag[xxx][yyy] != 'R':
                        cnt[2] += 1
            sum_cnt = sum(cnt)
            if min_flag > sum_cnt:
                min_flag = sum_cnt
    print(f'#{tc} {min_flag}')



# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     flag = list([j for j in input()] for i in range(N))
#     num_W = [0]*N
#     num_B = [0]*N
#     num_R = [0]*N
#     for i in range(N):
#         for j in range(M):
#             if flag[i][j] != 'W':
#                 num_W[i] += 1
#             if flag[i][j] != 'B':
#                 num_B[i] += 1
#             if flag[i][j] != 'R':
#                 num_R[i] += 1
#     print(num_W, num_B, num_R)

