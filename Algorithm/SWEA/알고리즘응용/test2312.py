parent = dict()
rank = dict()
graph = {
    'vertices': [0, 1, 2, 3, 4, 5, 6],
    'edges' :[(7, 0, 1),
        (7, 3, 4),
        (2, 5, 1),
        (5, 4, 1),
        (2, 0, 6),
        (5, 5, 1),
        (1, 0, 6),
        (9, 6, 1),
        (8, 3, 1),
        (2, 2, 1),
        (5, 5, 6),
]
}

def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)
        # print('mst:', mst)

    return mst
res = 0
print(kruskal(graph))
for k in kruskal(graph):
    res += k[0]
print(parent)
print(rank)
print(res)

# def countingsort(before, After, k):
#     temp = [0] * k
#
#     for i in range(0, len(After)):
#         temp[before[i]] += 1
#
#     for i in range(1, len(C)):
#         temp[i] += temp[i - 1]
#
#     for i in range(len(After)-1, -1, -1):
#         After[temp[before[i]] - 1] = before[i]
#         temp[before[i]] -= 1
#
# a = [23, 4, 6, 1, 44, 23, 22, 7, 1]
# b = [0] * len(a)
# countingsort(a, b, max(a)+1)