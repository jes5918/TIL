import sys
sys.stdin = open('1238.txt', 'r')

def bfs(x):
    q = []
    q.append(x)
    visited[x] = 1
    while q:
        x = q.pop(0)
        for nx in range(1, 101):
            if arr[x][nx] and not visited[nx]:
                q.append(nx)
                visited[nx] = visited[x] + 1

for tc in range(1, 11):
    N, st = map(int, input().split())
    lines = list(map(int, input().split()))
    arr = [[False]*101 for i in range(101)]
    visited = [0] * 101
    for i in range(0, N, 2):
        arr[lines[i]][lines[i+1]] = True
    bfs(st)
    maxx = 0
    res = 0
    for idx, num in enumerate(visited):
        if maxx < num:
            maxx = num
            res = idx
        elif maxx == num:
            res = idx
    print('#{} {}'.format(tc, res))