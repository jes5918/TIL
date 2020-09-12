import sys
sys.stdin = open('5174.txt', 'r')

def LPR(x):
    global cnt
    if L[x]:
        cnt += 1
        LPR(L[x])
    if R[x]:
        cnt += 1
        LPR(R[x])

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    L = [False] * (E+2)
    R = [False] * (E+2)
    for i in range(E):
        a = data[i*2]
        b = data[i*2+1]
        if not L[a]:
            L[a] = b
        else:
            R[a] = b
    cnt = 1
    LPR(N)
    print('#{} {}'.format(tc, cnt))