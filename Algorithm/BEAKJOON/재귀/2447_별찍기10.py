def eraser(id):
    for i in id:
        for j in id:
            board[i][j] = " "
    return

N = int(input())
board = [['*'] * N for _ in range(N)]
k = N
count = 0
while k != 0:
    k //= 3
    count += 1

for c in range(count):
    idx = []
    for i in range(N):
        if (i // 3 ** c) % 3 == 1:
            idx.append(i)
    eraser(idx)

for i in range(N):
    print(''.join(board[i]))


# def star(N):
#     global n
#     global basic
#     if n == 3:
#         return basic
#     arr = ['' for _ in range(N * 3)]
#     for i in range(N*3//N):
#         if i == 1:
#             for j in range(len(basic)):
#                 arr[N * i + j] = basic[j] + ' ' * len(basic[j]) + basic[j]
#         else:
#             for j in range(len(basic)):
#                 arr[N * i + j] = basic[j] * 3
#     basic = arr
#     if N*3 == n:
#         return basic
#     else:
#         return star(N*3)
#
# basic =['***','* *','***']
# n = int(input())
# k = star(3)
# for p in k:
#     print(p)