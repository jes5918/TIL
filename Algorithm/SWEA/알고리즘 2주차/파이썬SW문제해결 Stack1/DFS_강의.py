import sys
sys.stdin = open("input.txt", "r")

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

N, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0] * (N + 1) for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)