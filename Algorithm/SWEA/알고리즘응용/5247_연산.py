import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000000)

def BFS(now, cnt):
    global res
    q = deque()
    q.append((now, cnt))
    while q:
        nn, cc = q.popleft()
        for x in [nn + 1, nn - 1, nn * 2, nn - 10]:
            if x == M:
                if res > cc:
                    res = cc
                continue
            if cc > res:
                continue
            q.append((x, cc+1))


for tc in range(1, int(input().rstrip())+1):
    N, M = map(int, input().rstrip().split())
    res = 987654321
    BFS(N, 0)
    print('#{} {}'.format(tc, res))