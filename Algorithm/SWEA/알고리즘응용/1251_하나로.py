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


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


for tc in range(1, int(input().rstrip()) + 1):
    # 입력부분
    N = int(input().rstrip())
    x_point = list(map(int, input().rstrip().split()))
    y_point = list(map(int, input().rstrip().split()))
    E = float(input().rstrip())
    # 섬 입력받기
    arr = list(zip(x_point, y_point))

    # 그래프 만들기
    G = []
    for i in range(N):
        for j in range(i + 1, N):
            G += [(E * ((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2), i, j)]

    # 크루스칼 알고리즘
    parent = dict()
    rank = dict()

    # 노드 초기화
    for node in range(N):
        make_set(node)

    # 그래프 정렬
    G.sort()

    # 유니온 과정
    res = 0
    for g in G:
        weight, node_v, node_u = g
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            res += weight

    print('#{} {}'.format(tc, round(res)))

# 프림알고리즘 훨씬빠름
# def hanaro(N):
#     check = [0xffffffffffff]*N
#     check[0] = 0
#     visit = [0]*N
#     total_length = 0
#
#     for _ in range(N):
#         # 시작점 찾기
#         cur = -1
#         min_value = 0xffffffffffff
#         for i in range(N):
#             if visit[i]: continue
#             if check[i] < min_value:
#                 cur, min_value = i, check[i]
#
#         visit[cur] = 1
#         total_length += min_value
#
#         for j in range(N):
#             if cur == j: continue
#             dist_bet = (x_list[j]-x_list[cur])**2 + (y_list[j]-y_list[cur])**2
#             if dist_bet < check[j]:
#                 check[j] = dist_bet
#     return total_length
#
#
# T = int(input())
# for tc in range(1,1+T):
#     N = int(input())
#     x_list = list(map(int, input().split()))
#     y_list = list(map(int, input().split()))
#     E = float(input())
#     ans = round(hanaro(N) * E)
#     print('#{} {}'.format(tc, ans))





# 처음 다익스트라로 잘못알고풀어 모든경로를 안찍고 거리를 꼐산 아주 틀린방법
#
# def BFS(x, y):
#     q = deque()
#     q.append([x, y])
#     while q:
#         now_dist, now = q.popleft()
#         for next_idx, distance in G[now]:
#             if dist[next_idx] > now_dist + distance:
#                 dist[next_idx] = now_dist + distance
#                 q.append([dist[next_idx], next_idx])
#
#
# for tc in range(1, int(input().rstrip())+1):
#     # 입력부분
#     N = int(input().rstrip())
#     x_point = list(map(int, input().rstrip().split()))
#     y_point = list(map(int, input().rstrip().split()))
#     E = float(input().rstrip())
#     # 섬 입력받기
#     arr = list(zip(x_point, y_point))
#
#     # 그래프 만들기
#     G = [[] for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if i != j:
#                 G[i] += [(j, int(E * ((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)))]
#
#     # 거리 배열 초기화
#     dist = [987654321 for _ in range(N)]
#     dist[0] = 0
#     BFS(0, 0)
#     print(dist)
#     print('#{} {}'.format(tc, dist[N-1]))
