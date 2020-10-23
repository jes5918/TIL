import sys, time
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(50000)
start = time.time()

# BFS는 시간초과가 난다.... DFS로 해야지
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

delta = [(1, 0), (0, 1)]
def DFS(x, y, total):
    global result
    total += board[x][y]
    if result < total:
        return
    if x == N-1 and y == N-1:
        result = total
        return
    for a, b in delta:
        nx = a + x
        ny = b + y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        DFS(nx, ny, total)
        visited[nx][ny] = False

for tc in range(1, int(input())+1):
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    result = 987654321
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    DFS(0, 0, 0)
    print('#{} {}'.format(tc, result))

print(time.time()-start)