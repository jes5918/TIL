from collections import  defaultdict
from heapq import *

myedges = [
    (7, 'A', 'B'),
    (7, 'D', 'E'),
    (2, 'F', 'B'),
    (5, 'E', 'B'),
    (2, 'A', 'G'),
    (5, 'F', 'B'),
    (1, 'A', 'G'),
    (9, 'G', 'B'),
    (8, 'D', 'B'),
    (2, 'C', 'B'),
    (5, 'F', 'G'),

]

def prim(start_node, edges):
    mst = list()
    adjacent_edge = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edge[n1].append((weight, n1, n2))
        adjacent_edge[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edge[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edge[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    return mst
res = 0
print(prim('A', myedges))
for a in prim('A', myedges):
    res += a[0]
print(res)
