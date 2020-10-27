def bt(a, k, p):
    global best
    if best >= p:
        return
    elif k == n:
        best = p
    else:
        for i in range(k, n):
            a[k], a[i] = a[i], a[k]
            bt(a, k + 1, p * g[k][a[k]] / 100)
            a[k], a[i] = a[i], a[k]


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    best = 0
    bt([i for i in range(n)], 0, 1)
    print("#{0} {1:.6f}".format(test_case, best * 100))
