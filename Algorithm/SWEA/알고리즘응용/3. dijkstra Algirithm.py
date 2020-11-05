from heapq import *

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5},
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    print(distances)
    distances[start] = 0
    q = []
    heappush(q, [distances[start], start])

    while q:
        current_distance, current_node = heappop(q)
        if distances[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heappush(q, [distance, adjacent])
    print(distances)
    return distance


def dijkstra2(G, r):
    D = [float('inf')] * N
    P = [None] * N
    visited = [False] * N
    D[r] = 0
    for _ in range(N):
        minidx = -1
        minval = 0xffffffff
        for i in range(N):
            if not visited[i] and D[i] < minval:
                minval = D[i]
                minidx = i
        visited[minidx] = True
        for v, val in G[minidx]:
            if not visited[v] and D[minidx] + val < D[v]:
                D[v] = D[minidx] + val
                P[v] = minidx


print(dijkstra(mygraph, 'A'))
