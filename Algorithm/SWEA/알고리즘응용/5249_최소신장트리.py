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