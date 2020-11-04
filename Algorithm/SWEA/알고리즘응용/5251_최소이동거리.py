import sys
from collections import deque
sys.stdin = open('input9.txt', 'r')
# dijkstra에 적합한문제
# 최단경로를 찾는 알고리즘
# 출발지부터 목적지까지의 최단 경로를 찾기 위한 알고리즘
# 출발지부터 목적지까지 가능 다양한 경로의 가중치를 누적하여 최소의 노력으로 목적지까지 가는 방식
def BFS(x, y):
    q = deque()
    q.append([x, y])
    while q:
        now_dist, now = q.popleft()
        for next_idx, distance in G[now]:
            if dist[next_idx] > now_dist + distance:
                dist[next_idx] = now_dist + distance
                q.append([dist[next_idx], next_idx])

for tc in range(1, int(input().rstrip())+1):
    N, E = map(int, input().rstrip().split())
    G = [[] for _ in range(N+1)]
    dist = [987654321 for _ in range(N+1)]
    dist[0] = 0
    for _ in range(E):
        s, e, w = map(int, input().rstrip().split())
        G[s].append((e, w))
    BFS(0, 0)
    print('#{} {}'.format(tc, dist[N]))
