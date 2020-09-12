import sys
sys.stdin = open('7465.txt', 'r')

# def changdragon(x, y):
#     q = []
#     q.append((x,y))
#     while q:
#         xx, yy = q.pop(0)
#         friend[xx][yy] = False
#         for i in range(1, N+1):
#             if friend[yy][i]:
#                 q.append((yy, i))
#     return
#
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     friend = [[False] * (N+1) for _ in range(N+1)]
#     for i in range(M):
#         m1, m2 = map(int, input().split())
#         friend[m1][m2] = True
#     result = 0
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if friend[i][j]:
#                 changdragon(i, j)
#                 result += 1
#     print(friend)
#     print('#{} {}'.format(tc, result))

def dfs(a):
    visited[a] = True
    for b in friends[a]:
        if not visited[b]:
            dfs(b)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    friends = [[] for _ in range(N+1)]
    visited = [False]*(N+1)
    for _ in range(M):
        m1, m2 = map(int, input().split())
        friends[m1].append(m2)
        friends[m2].append(m1)

    res = 0
    for x in range(1, N+1):
        if not visited[x]:
            dfs(x)
            res += 1
    print('#{} {}'.format(tc, res))


# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     friend = []
#     for _ in range(M):
#         m1, m2 = map(int, input().split())
#         friend.append([m1, m2])
#     temp = [[x for x in f] for f in friend]
#     for idx in range(M):
#         start = temp[idx][0]
#         point = temp[idx][1]
#         temp[idx][1] = start
#         for i in range(M):
#             for j in range(2):
#                 if point == friend[i][j]:
#                     temp[i][j] = start
#     for a in range(M):
#         for b in range(2):
#             if temp[a][b] == friend[-1][-1]:
#                 temp[a][b] = temp[-1][1]
#     res = []
#     for t in temp:
#         if t not in res:
#             res.append(t)
#     print('#{} {}'.format(tc, len(res)))
