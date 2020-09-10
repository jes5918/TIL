T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input().split()] for y in range(N)]
    dxdy = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    res = []
    for x in range(N):
        for y in range(N):
            tmp = []
            cnt = 1
            tmp.append([x, y])
            while tmp:
                [xx, yy] = tmp.pop()
                for a, b in dxdy:
                    pointX = xx + a
                    pointY = yy + b
                    if N > pointX >= 0 and N > pointY >= 0:  # 상하좌우 index 값이 0보다 같거나크고 N보다 작을때
                        if arr[xx][yy] + 1 == arr[pointX][pointY]:
                            tmp.append([pointX, pointY])
                            cnt += 1
                            break
            res += [[arr[x][y], cnt]]
    res = sorted(res, key = lambda x : (-x[1], x[0]))
    print(f'#{tc} {res[0][0]} {res[0][1]}')

# import sys
# sys.stdin = open("input2.txt", "r")
#
# def udlr(xx, yy, cnt, aa, bb):
#     for i in range(4):
#         pointX = xx + dx[i]
#         pointY = yy + dy[i]
#         if N > pointX >= 0 and N > pointY >= 0:  # 상하좌우 index 값이 0보다 같거나크고 N보다 작을때
#             if arr[xx][yy] + 1 == arr[pointX][pointY]:
#                 if cnt == 1:
#                     aa, bb = xx, yy
#                 cnt += 1
#                 return udlr(pointX, pointY, cnt, aa, bb)
#     else:
#         maxcnt_num[arr[aa][bb]] = cnt
#         return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[int(x) for x in input().split()] for y in range(N)]
#     dx = [0, 0, -1, 1] # 위 아래
#     dy = [-1, 1, 0, 0] # 좌 우
#     maxcnt_num = {}
#     count = 1
#     aa = 0
#     bb = 0
#     for x in range(N):
#         for y in range(N):
#             count = 1
#             udlr(x, y, count, aa, bb)
#
#     res_arr = []
#     for x, y in maxcnt_num.items():
#          res_arr.append((x, y))
#
#     MAX = -1
#     MAX_idx = -1
#     for k in res_arr:
#         if MAX < k[1]:
#             MAX = k[1]
#             MAX_idx = k[0]
#         elif MAX == k[1]:
#             if MAX_idx > k[0]:
#                 MAX = k[1]
#                 MAX_idx = k[0]
#     print(f'#{tc} {MAX_idx} {MAX}')


# 교수님풀이

# dx=[0, 1, 0, -1]
# dy=[1, 0, -1, 0]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr= [list(map(int, input().split())) for i in range(N)]
#     MAX=0
#     num=0
#     q = []
#
#     for i in range(N):
#         for j in range(N):
#             q.append([i, j])
#             cnt = 1
#
#             while q:
#                 [x, y] = q.pop()
#                 for k in range(4):
#                     xx = x+dx[k]
#                     yy = y+dy[k]
#
#                     if 0<=xx<N and 0<=yy<N:
#                         if arr[xx][yy]==arr[x][y]+1:
#                             cnt+=1
#                             q.append([xx,yy])
#
#             if MAX==cnt and arr[i][j]<num:
#                 num = arr[i][j]
#
#             if MAX<cnt:
#                 MAX=cnt
#                 num = arr[i][j]
#
#     print('#{} {} {}'.format(tc, num, MAX))