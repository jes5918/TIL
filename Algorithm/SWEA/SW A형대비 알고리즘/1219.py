import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):
    global res
    visited[v] = 1
    for r in route:
        if r[v] != 0 and visited[r[v]] == 0:
            if r[v] == 99:
                result = 1
            dfs(r[v])


for T in range(10):
    tc, n = map(int, input().split())
    arr = list(map(int, input().split()))
    route = [[0] * 100 for _ in range(2)]
    res = 0
    visited = [0] * 100
    for i in range(n):
        st, end = arr[2 * i], arr[2 * i + 1]
        if route[0][st]:
            route[1][st] = end
        else:
            route[0][st] = end
    dfs(0)

    print('#{} {}'.format(tc, res))
# def find_destination(node):
#     a = b = 0
#     if arr1[node] == 99 or arr2[node] == 99:
#         return 1
#
#     if arr1[node] != -1:
#         temp = arr1[node]
#         arr1[node] = -1
#         a = find_destination(temp)
#     if arr2[node] != -1:
#         temp = arr2[node]
#         arr2[node] = -1
#         b = find_destination(temp)
#
#     if a == 1 or b == 1:
#         return 1
#     else:
#         return 0
#
# for _ in range(10):
#     tc, N = map(int, input().split())
#     L = list(map(int, input().split()))
#     arr1 = [-1] * 100
#     arr2 = [-1] * 100
#     for x in range(0, N*2, 2):
#         if arr1[L[x]] == -1:
#             arr1[L[x]] = L[x+1]
#         else:
#             arr2[L[x]] = L[x+1]
#     print('#{} {}'.format(tc, find_destination(0)))