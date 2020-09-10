import sys
sys.stdin = open('5176.txt', 'r')
def LPR(x):
    global numbering
    if L[x]:
        LPR(L[x])
    P[x] = numbering
    numbering += 1
    if R[x]:
        LPR(R[x])

for tc in range(1, int(input())+1):
    N = int(input())
    L = [False] * (N+1)
    R = [False] * (N+1)
    P = [False] * (N+1)
    cnt = N-1
    i = 0
    while True:
        i += 1
        L[i] = i * 2
        cnt -= 1
        if cnt == 0:
            break
        R[i] = i * 2 + 1
        cnt -= 1
        if cnt == 0:
            break
    numbering = 1
    LPR(1)
    print('#{} {} {}'.format(tc, P[1], P[N//2]))