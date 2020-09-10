import sys
sys.stdin = open('1861.txt', 'r')

def bfs(x, y):
    cnt = 1
    q = []
    q.append((x, y))
    while q:
        xx, yy = q.pop(0)
        for a, b in delta:
            nx = a + xx
            ny = b + yy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if borad[xx][yy] + 1 == borad[nx][ny]:
                q.append((nx, ny))
                cnt += 1
                break
    return cnt

for tc in range(1, int(input())+1):
    N = int(input())
    borad = [[int(x) for x in input().split()] for _ in range(N)]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    res = []
    for i in range(N):
        for j in range(N):
            res.append([borad[i][j], bfs(i, j)])
    res.sort(key=lambda x: (-x[1], x[0]))
    print('#{} {} {}'.format(tc, res[0][0], res[0][1]))
