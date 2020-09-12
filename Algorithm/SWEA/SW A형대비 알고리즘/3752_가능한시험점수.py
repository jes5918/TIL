import sys
sys.stdin = open('3752.txt', 'r')

def exampoints(n, summ):
    res.append(summ)
    if n == N:
        return
    exampoints(n+1, summ + points[n])
    exampoints(n+1, summ)

for tc in range(1, int(input())+1):
    N = int(input())
    points = list(map(int, input().split()))
    res = []
    exampoints(0, 0)
    res = set(res)
    print('#{} {}'.format(tc, len(res)))