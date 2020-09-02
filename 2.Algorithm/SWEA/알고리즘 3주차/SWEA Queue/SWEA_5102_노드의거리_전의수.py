import sys
sys.stdin = open('5102.txt', 'r')

def bfs(x, G):
    q = []
    visited = [0] * (V + 1)
    q.append(x)
    visited[x] = 1
    while q:
        x = q.pop(0)
        for nx in range(1, V+1):
            if arr[x][nx] and not visited[nx]:
                q.append(nx)
                visited[nx] = visited[x] + 1
                if nx == G:
                    return visited[nx] - 1

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for i in range(V+1)]
    for i in range(E):
        st, ed = map(int, input().split())
        arr[st][ed] = arr[ed][st] = 1
    S, G = map(int, input().split())
    res = bfs(S, G)
    if not res:
        res = 0
    print('#{} {}'.format(tc, res))