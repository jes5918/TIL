import sys
sys.stdin = open('1231.txt', 'r')

def LPR(x):
    if L[x]:
        LPR(L[x])
    print(P[x], end='')
    if R[x]:
        LPR(R[x])

for tc in range(1, 11):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)
    for _ in range(N):
        data = list(input().split())
        if len(data) == 4:
            L[int(data[0])] = int(data[2])
            R[int(data[0])] = int(data[3])
            P[int(data[0])] = data[1]
        elif len(data) == 3:
            L[int(data[0])] = int(data[2])
            P[int(data[0])] = data[1]
        else:
            P[int(data[0])] = data[1]

    print('#{}'.format(tc), end=' ')
    LPR(1)
    print()