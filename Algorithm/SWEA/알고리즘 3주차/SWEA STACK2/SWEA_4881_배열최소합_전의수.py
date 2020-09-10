import sys
sys.stdin = open("input4.txt", "r")

def perm(idx):
    global sub_res, res
    if res < sub_res:
        return
    if idx == N:
        if sub_res < res:
            res = sub_res
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            sub_res += array[idx][i]
            perm(idx+1)
            visited[i] = False
            sub_res -= array[idx][i]

for tc in range(1, int(input())+1):
    N = int(input())
    visited = [False] * N
    array = [[int(x) for x in input().split()] for _ in range(N)]
    sub_res, res = 0, 987654321
    perm(0)
    print('#{} {}'.format(tc, res))

# 런타임에러 났다,,,,
# def perm(idx):
#     if idx == N:
#         temp = [False] * N
#         for i in range(N):
#             temp[i] = sel[i]
#         index_list.append(temp)
#         return
#     for i in range(N):
#         if not visited[i]:
#             sel[idx] = arr[i]
#             visited[i] = True
#             perm(idx+1)
#             visited[i] = False
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [i for i in range(N)]
#     sel = [False for j in range(N)]
#     visited = [False] * N
#     index_list = []
#     array = [[int(x) for x in input().split()] for _ in range(N)]
#     perm(0)
#     res = []
#     for i in range(len(index_list)):
#         temp = 0
#         for j in range(N):
#             temp += array[j][index_list[i][j]]
#         res.append(temp)
#     print('#{} {}'.format(tc, min(res)))
