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

cnt=1
arr=[[0]*5 for i in range(5)]

row_start=0
row_end=4
col_start=0
col_end=4

while row_start<=row_end and col_start<=col_end:
    # 왼쪽=> 오른쪽
    for i in range(col_start, col_end+1):
        arr[row_start][i]=cnt
        cnt+=1
    row_start +=1

    # 위=> 아래
    for i in range(row_start, row_end + 1):
        arr[i][col_end] = cnt
        cnt += 1
    col_end -= 1

    # 오른쪽=> 왼쪽
    for i in range(col_end, col_start-1, -1):
        arr[row_end][i]=cnt
        cnt+=1
    row_end -=1

    # 아래=> 위
    for i in range(row_end, row_start - 1, -1):
        arr[i][col_start] = cnt
        cnt += 1
    col_start += 1

print(arr)