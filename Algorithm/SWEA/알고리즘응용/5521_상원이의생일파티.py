import sys

sys.stdin = open('input12.txt', 'r')
from collections import deque

def sangwon(i, nn):
    q = deque()
    q.append((i, nn))
    while q:
        idx, n = q.popleft()
        if n == 2:
            continue
        for a in arr[idx]:
            if not visited[a]:
                visited[a] = 1
                q.append((a, n+1))


for tc in range(1, int(input().rstrip()) + 1):
    N, M = map(int, input().rstrip().split())
    arr = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        arr[a] += [b]
        arr[b] += [a]
    sangwon(1, 0)
    print('#{} {}'.format(tc, sum(visited)-visited[1]))
