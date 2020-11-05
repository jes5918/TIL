import sys
sys.stdin = open('input7.txt', 'r')

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



for tc in range(1, int(input().rstrip())+1):
    N, K = map(int, input().rstrip().split())
    G = [list(map(int, input().rstrip().split())) for _ in range(K)]
    # 정렬과정 (가중치로)
    G.sort(key=lambda x: x[2])

    # 크루스칼 알고리즘
    parent = dict()
    rank = dict()

    # 노드 초기화
    for n in range(N+1):
        make_set(n)

    #유니온 과정
    res = 0
    for g in G:
        a, b, w = g
        if find(a) != find(b):
            union(a, b)
            res += w
    print('#{} {}'.format(tc, res))

# 프림방법
# def prim(G):
#     visited = [False for _ in range(V + 1)]
#     dist = [float('inf') for _ in range(V + 1)]
#     dist[0] = 0
#     for _ in range(V + 1):
#         minval = 0xfffffffffff
#         start = -1
#         for i in range(V + 1):
#             if dist[i] < minval and not visited[i]:
#                 minval = dist[i]
#                 start = i
#         visited[start] = True
#         for next, weight in G[start]:
#             if weight < dist[next] and not visited[next]:
#                 dist[next] = weight
#     return sum(dist)
#
# for tc in range(1, int(input().rstrip())+1):
#     V, E = map(int, input().rstrip().split())
#     G = [[] for _ in range(V + 1)]
#     for _ in range(E):
#         n1, n2, w = map(int, input().rstrip().split())
#         G[n1] += [(n2, w)]
#         G[n2] += [(n1, w)]
#     print('#{} {}'.format(tc, prim(G)))