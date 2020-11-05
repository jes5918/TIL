import sys
from collections import deque
# sys.stdin = open('input9.txt', 'r')

def find_p(x):
    if x != p[x]:
        p[x] = find_p(p[x])
    return p[x]

def union(node_v, node_u):
    root1 = find_p(node_v)
    root2 = find_p(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

rank = dict()
dst = dict()
p = list(range(8))
dst = [(7, 0, 1),
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
dst.sort()
cnt = 0
total = 0
res = []
mst = []

for d in dst:
    weight, node_v, node_u = d
    if find_p(node_v) != find_p(node_u):
        union(node_v, node_u)
        mst.append(edge)

print(p)
print(res)
print(mst)
# print('#{} {}'.format(1, total))