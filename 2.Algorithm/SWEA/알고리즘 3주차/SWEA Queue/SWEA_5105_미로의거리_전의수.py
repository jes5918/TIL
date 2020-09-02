import sys
sys.stdin = open('5105.txt', 'r')

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def findstart(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs(x, y, N):
    q = []
    visited = [[0]*N for _ in range(N)]
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.pop(0)
        if array[x][y] == 3:
            return visited[x][y] - 2
        for a, b in delta:
            nx = a + x
            ny = b + y
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if array[nx][ny] != 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

for tc in range(1, int(input())+1):
    N = int(input())
    array = [[int(x) for x in input()] for _ in range(N)]
    a, b = findstart(array)
    res = bfs(a, b, N)
    if not res:
        res = 0
    print('#{} {}'.format(tc, res))