import sys

def NM1(idx):
    if idx == M:
        print(*sel)
        return
    else:
        temp = 0

    for i in range(N):
        # if visited[i] == 1:
        #     continue
        if temp == NN[i]:
            continue
        # if sel:
        #     if NN[i] < max(sel):
        #         continue
        visited[i] = 1
        temp = NN[i]
        sel.append(NN[i])
        NM1(idx + 1)
        visited[i] = 0
        sel.pop()

N, M = map(int, sys.stdin.readline().split())
NN = [int(x) for x in input().split()]
NN.sort()
sel = []
visited = [0] * N
NM1(0)
