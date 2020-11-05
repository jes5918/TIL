# 처음엔 다익스트라로 풀라고 생각했지만
# 다익스트라는 모든 경로를안가고 출발지부터 목적지까지 최단거리로 갈 수 있는 경우를 찾는 것이기 때문에
#
# 최소신장트리 방법 사용
# 그래프의 속성을 가지고 있으며 간선에 가중치를 추가 한 그래프의 하위 개념인 트리
# 최소한의 비용으로 모든 도시를 연결하는 도로를 설계하는 문제를 풀기 적합한 알고리즘
# 간선의 가중치를 기준으로 사이클을 제거하여 필요한 정보만 가지는 방식
# 가장 작은 가중치를 가지는 트리를 만드는 알고리즘

# - 프림(Prim) 알고리즘 : 정점에 연결 된 간선의 가중치 중 가장 작은 가중치의 간선을 연결해 나가는 방식
# - 크루스칼(kruskal) 알고리즘 : 모든 간선의 가중치를 조사하고 정렬 후 순서대로 연결해 나가는 방식
#
# - 최소 신장 트리에서 발생하는 사이클은 깊이 우선 탐색 방법으로 해결할 수 있지만 성능 저하
# - 분리 집합을 이용하여 해당하는 연결 되지 않은 정점을 순서대로 연결해 나가는 방식 선호
import sys

sys.stdin = open('input11.txt', 'r')


# 프림알고리즘 훨씬빠름
def prim():
    dist = [0xfffffffffffff] * N
    dist[0] = 0
    visited = [False] * N
    total = 0
    for _ in range(N):
        current = -1
        minval = 0xffffffffffff
        for i in range(N):
            if not visited[i] and dist[i] < minval:
                current = i
                minval = dist[i]

        visited[current] = True
        total += minval

        for i in range(N):
            if current != i:
                dist_bet = (x_point[i] - x_point[current]) ** 2 + (y_point[i] - y_point[current]) ** 2
                if dist_bet < dist[i]:
                    dist[i] = dist_bet
    return total


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    x_point = list(map(int, input().split()))
    y_point = list(map(int, input().split()))
    E = float(input())
    print('#{} {}'.format(tc, round(prim() * E)))
