import sys
sys.stdin = open('input7.txt', 'r')

def prim(G):
    visited = [False for _ in range(V + 1)]
    dist = [float('inf') for _ in range(V + 1)]
    dist[0] = 0
    for _ in range(V + 1):
        minval = 0xfffffffffff
        start = -1
        for i in range(V + 1):
            if dist[i] < minval and not visited[i]:
                minval = dist[i]
                start = i
        visited[start] = True
        for next, weight in G[start]:
            if weight < dist[next] and not visited[next]:
                dist[next] = weight
    return sum(dist)

for tc in range(1, int(input().rstrip())+1):
    V, E = map(int, input().rstrip().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().rstrip().split())
        G[n1] += [(n2, w)]
        G[n2] += [(n1, w)]
    print('#{} {}'.format(tc, prim(G)))