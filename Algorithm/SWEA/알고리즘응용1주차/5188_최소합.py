import sys, time
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(50000)
start = time.time()

# delta = [(1, 0), (0, 1)]
# def BFS(x, y, d):
#     global result
#     q = [(x, y, d)]
#     while q:
#         a, b, c = q.pop(0)
#         c += board[a][b]
#         if c > result:
#             continue
#         if a == N - 1 and b == N - 1:
#             if result > c:
#                 result = c
#         for aa, bb in delta:
#             nx = aa + a
#             ny = bb + b
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                 continue
#             q.append((nx, ny, c))
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     board = [[int(x) for x in input().split()] for _ in range(N)]
#     result = 987654321
#     BFS(0, 0, 0)
#     print('#{} {}'.format(tc, result))

print(time.time()-start)