import sys
sys.stdin = open('4613.txt', 'r')

def coloring():
    global minn
    wc, bc, rc = 0, 0, 0
    for i in W:
        wc += M - i.count('W')
    for i in B:
        bc += M - i.count('B')
    for i in R:
        rc += M - i.count('R')
    if minn > (wc + bc + rc):
        minn = (wc + bc + rc)


for t in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    WBR = [input() for _ in range(N)]
    minn = N * M
    for i in range(1, N - 1):
        for j in range(1, i + 1):
            W = WBR[0:j]
            B = WBR[j:(N - i + j - 1)]
            R = WBR[(N - i + j - 1):N]
            coloring()
    print('#{} {}'.format(t, minn))
