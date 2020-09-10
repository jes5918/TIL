# def rotate90(m):
#     num = len(m)
#     res = [[0] * N for _ in range(num)]
#
#     for r in range(num):
#         for c in range(num):
#             res[num-1-c][r] = m[r][c]
#     return res
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [num for num in range(1, N**2 + 1)]
#     dalpang = [[0 for j in range(N)] for i in range(N)]
#     cnt_squre = 0
#     cnt = N-1
#     while True:
#         temp1 = arr[:cnt + 1]
#         arr = arr[cnt+1:]
#         try:
#             for i in range(cnt+1):
#                 dalpang[cnt_squre][cnt_squre+i] = temp1[i]
#         except:
#             break
#         dalpang = rotate90(dalpang)
#
#         temp2 = arr[:cnt]
#         arr = arr[cnt:]
#         try:
#             for i in range(1, cnt+1):
#                 dalpang[cnt_squre][cnt_squre+i] = temp2[i-1]
#         except:
#             dalpang = rotate90(dalpang)
#             dalpang = rotate90(dalpang)
#             dalpang = rotate90(dalpang)
#             break
#         dalpang = rotate90(dalpang)
#
#         temp3 = arr[:cnt]
#         arr = arr[cnt:]
#         try:
#             for i in range(1, cnt+1):
#                 dalpang[cnt_squre][cnt_squre+i] = temp3[i-1]
#         except:
#             dalpang = rotate90(dalpang)
#             dalpang = rotate90(dalpang)
#             break
#         dalpang = rotate90(dalpang)
#
#         temp4 = arr[:cnt - 1]
#         arr = arr[cnt-1:]
#         try:
#             for i in range(1, cnt):
#                 dalpang[cnt_squre][cnt_squre+i] = temp4[i-1]
#         except:
#             dalpang = rotate90(dalpang)
#             break
#         dalpang = rotate90(dalpang)
#
#         cnt_squre += 1
#         cnt -= 1
#     print(dalpang)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    dalpang = [[0 for j in range(N)] for i in range(N)] # 배열 0으로 초기화

    r_st = 0
    r_end = N-1
    c_st = 0
    c_end = N-1

    while c_st <= c_end and r_st <= r_end:
        for i in range(c_st, c_end+1):  # 왼쪽에서 오른쪽
            dalpang[r_st][i] = cnt
            cnt += 1
        r_st += 1

        for i in range(r_st, r_end + 1): # 위에서 아래
            dalpang[i][c_end] = cnt
            cnt += 1
        c_end -= 1

        for i in range(c_end, c_st-1, -1): # 오른쪽에서 왼쪽
            dalpang[r_end][i] = cnt
            cnt += 1
        r_end -= 1

        for i in range(r_end, r_st - 1, -1): # 아래에서 위쪽
            dalpang[i][c_st] = cnt
            cnt += 1
        c_st += 1

    print(f'#{tc}')
    for i in range(N):
        print(*dalpang[i]) # 아주 좋아 이 표현식