import sys
sys.stdin = open('1226.txt', 'r')

# dfs풀이
def dfs(x, y):
    global res
    if (x, y) == (13, 13):
        res = 1
        return
    visited.append((x, y))
    for a, b in delta:
        nx = a + x
        ny = b + y
        if 0 <= nx < 16 and 0 <= ny < 16 and (arr[nx][ny] == 0 or arr[nx][ny] == 3) and ((nx, ny) not in visited):
            dfs(nx, ny)

# bfs 풀이
def bfs(x, y, n):
    global res
    q = []
    q.append((x, y))
    visited = [[0] * N for i in range(N)]
    visited[x][y] = 1
    while q:
        (x, y) = q.pop(0)
        if arr[x][y] == 3:
            res = 1
            return
        for a, b in delta:
            nx = a + x
            ny = b + y
            if arr[nx][ny] != 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return 0

for tc in range(10):
    N = 16
    test_case = int(input())
    arr = [[int(x) for x in input()] for _ in range(16)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = 0
    # dfs(1, 1)
    bfs(1, 1, N)
    print('#{} {}'.format(test_case, res))


# dfs 풀이
# def dfs(x, y):
#     global res
#     if (x, y) == (13, 13):
#         res = 1
#         return
#     visited.append((x, y))
#     for a, b in delta:
#         nx = a + x
#         ny = b + y
#         if 0 <= nx < 16 and 0 <= ny < 16 and (arr[nx][ny] == 0 or arr[nx][ny] == 3) and ((nx, ny) not in visited):
#             dfs(nx, ny)
#
# for tc in range(10):
#     test_case = int(input())
#     arr = [[int(x) for x in input()] for _ in range(16)]
#     delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     res = 0
#     visited = []
#     dfs(1, 1)
#     print('#{} {}'.format(test_case, res))