import sys

def NM1(idx):
    if idx == M:
        print(*sel)
        return

    for i in range(N):
        sel.append(NN[i])
        NM1(idx + 1)
        sel.pop()

N, M = map(int, sys.stdin.readline().split())
NN = [int(x) for x in range(1, N+1)]
sel = []
NM1(0)

