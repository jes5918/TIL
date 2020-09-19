# import sys
# sys.setrecursionlimit(50000)
#
# def bfs(x, y):
#     global count, visited
#     visited[x][y] = 1
#     for aa, bb in delta:
#         nx = aa + x
#         ny = bb + y
#         if nx < 0 or nx >= M or ny < 0 or ny >= N:
#             continue
#         if arr[nx][ny] == -1:
#             continue
#         if visited[nx][ny]:
#             continue
#         if arr[nx][ny] == 1:
#             cnt.append(count)
#             count = 0
#             return
#         visited[nx][ny] = 1
#         count += 1
#         dfs(nx, ny)
#     return
#
#
# N, M = map(int, input().split())
# K = int(input())
#
# arr = [[0] * N]
# for _ in range(M-2):
#     arr.append([0] + [-1 for _ in range(N-2)] + [0])
# arr.append([0] * N)
#
# for _ in range(K):
#     a, b = map(int, input().split())
#     if a == 1:
#         arr[0][b] = 1
#     elif a == 2:
#         arr[M-1][b] = 1
#     elif a == 3:
#         arr[b][0] = 1
#     else:
#         arr[b][N-1] = 1
#
# px, py = map(int, input().split())
# delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# visited = [[0]*N for _ in range(M)]
# cnt = []
# count = 0
# dfs(px, py)
