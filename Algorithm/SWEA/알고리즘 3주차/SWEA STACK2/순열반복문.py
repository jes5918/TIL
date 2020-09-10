# N = 3
# array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# arr = [1, 2, 3]
# res = []
# for a in arr:
#     for b in arr:
#         if a == b:
#             continue
#         for c in arr:
#             if a == c or c == b:
#                 continue
#             res.append((a, b, c))
#
# sum_col = []
# for x in range(len(res)):
#     for j in range(N):
#         sum_col.append(array[j][res[x][j]])
#
# print(sum_col)

arr = [1, 2, 3]
N = 3
sel = [0] * N
visited = [0] * N

def perm(idx):
    if idx == N:
        print(sel)
        return
    for i in range(N):
        if not visited[i]:
            sel[idx] = arr[i]
            visited[i] = 1
            perm(idx + 1)
            visited[i] = 0
            # perm(idx+1)
perm(0)