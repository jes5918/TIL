def exampoints(n, summ):
    res.add(summ)
    if n == N:
        return
    exampoints(n+1, summ + points[n])
    exampoints(n+1, summ)

for tc in range(1, int(input())+1):
    N = int(input())
    points = list(map(int, input().split()))
    res = set()
    exampoints(0, 0)
    print('#{} {}'.format(tc, len(res)))