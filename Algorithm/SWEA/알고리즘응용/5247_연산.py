import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000000)


def BFS(now):
    q = deque()
    q.append(now)
    while q:
        nn = q.popleft()
        if nn == M:
            return
        for x in (nn + 1, nn - 1, nn * 2, nn - 10):
            if 0 < x <= 1000000 and not visited[x]:
                visited[x] = visited[nn] + 1
                q.append(x)


for tc in range(1, int(input().rstrip()) + 1):
    N, M = map(int, input().rstrip().split())
    visited = [0] * 1000001
    BFS(N)
    print('#{} {}'.format(tc, visited[M]))
