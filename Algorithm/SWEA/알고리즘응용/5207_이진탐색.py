import sys

sys.stdin = open('input7.txt', 'r')


def binarysearch():
    cnt = 0
    for b in B:
        l = 0
        r = N - 1
        before = 'start'
        while True:
            m = (l + r)//2
            if A[m] == b:
                cnt += 1
                break
            elif A[m] > b:
                r = m - 1
                now = 'right'
            elif A[m] < b:
                l = m + 1
                now = 'left'
            if now == before:
                break
            before = now
    return cnt

for tc in range(1, int(input().rstrip()) + 1):
    N, M = map(int, input().rstrip().split())
    A = sorted(list(map(int, input().rstrip().split())))
    B = list(map(int, input().rstrip().split()))
    print('#{} {}'.format(tc, binarysearch()))