import sys
sys.stdin = open('input9.txt', 'r')

# dijkstra에 적합한문제
# 최단경로를 찾는 알고리즘
# 출발지부터 목적지까지의 최단 경로를 찾기 위한 알고리즘
# 출발지부터 목적지까지 가능 다양한 경로의 가중치를 누적하여 최소의 노력으로 목적지까지 가는 방식

# 1. BFS를 이용한 다익스트라
# 이 방법은 오리지날 다익스트라 알고리즘 방법에 비해
# 완전탐색을 하면서 큐를 활용하기 떄문에 메모리와, 실행속도 증가
# 문제풀 생각이 나지 않으면 이 방법을 활용하는 것두 나쁘지않다
from collections import deque
def BFS_dijkstra(x, y):
    q = deque()
    q.append([x, y])
    while q:
        now_dist, now = q.popleft()
        for next_idx, distance in G[now]:
            if dist[next_idx] > now_dist + distance:
                dist[next_idx] = now_dist + distance
                q.append([dist[next_idx], next_idx])

# 2. 인덱스 값을 활용한 다익스트라 방법
# 이방법은 인덱스를 활용하기 때문에 BFS에 비해서
# 메모리와 실행속도가 더 적게 드는 장점이 있음
# 이 방법을 잘 숙지 한다면 효율성 테스트도 잘 활용할 수 있다.
def Origin_dijkstra(G, start):
    # 방문배열 초기화
    visited = [False] * (N + 1)
    # 거리배열 초기화
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    # 전체 노드 수 만큼 반복
    for _ in range(N):
        minidx = -1
        minval = 0xffffffff
        # 최소인덱스, 최소값 찾는 과정
        # 전체를 돌면서 다 봐야함(가장 최소 거리 찾아야 하기 때문)
        for i in range(N):
            if not visited[i] and dist[i] < minval:
                minval = dist[i]
                minidx = i
        # 최소값이 있는 곳 방문체크
        visited[minidx] = True

        # 최솟값이 저장되어 있는 그래프에 다음 노드를 위해 거리값 갱신
        for next, weight in G[minidx]:
            if not visited[next] and dist[minidx] + weight < dist[next]:
                dist[next] = dist[minidx] + weight
    return dist


for tc in range(1, int(input().rstrip()) + 1):
    N, E = map(int, input().rstrip().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().rstrip().split())
        G[s].append((e, w))
    # 1 번째 BFS 방법
    # BFS_dijkstra(0, 0)
    # 2 번째 dijkstra 방법
    dist = Origin_dijkstra(G, 0)
    print('#{} {}'.format(tc, dist[N]))
