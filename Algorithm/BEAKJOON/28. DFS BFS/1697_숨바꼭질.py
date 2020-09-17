from collections import deque

def bfs():
    q = deque()
    q.append(N)
    while q:
        n = q.popleft()
        if n == K:
            print(visited[n])
            return
        for nn in (n-1, n+1, n*2):
            if 0 <= nn < 100001 and not visited[nn]:
                visited[nn] = visited[n] + 1
                q.append(nn)

N, K = map(int, input().split())
visited = [0] * 100001
bfs()
