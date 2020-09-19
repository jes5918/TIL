def BFS(v):
    global count
    q = [v]
    while q:
        curr = q.pop(0)
        visited[curr] = 1
        for i in adj[curr]:
            if visited[i] == 0:
                visited[i] = 1
                count += 1
                q.append(i)

V = int(input())
E = int(input())

visited = [0]*(V+1)
adj = [[] for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
count = 0
BFS(1)
print(count)