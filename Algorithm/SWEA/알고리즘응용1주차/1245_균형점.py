import sys

sys.stdin = open('input.txt', 'r')


def balance(low, high, k, G):
    while high - low > (1 / (10 ** 12)):
        m = (low + high) / 2
        l, r = 0, 0
        for j in range(N):
            f = G * mass[k] * mass[j] / (point[j] - m) ** 2
            if point[j] < m:
                l += f
            else:
                r += f
        if l > r:
            low = m
        else:
            high = m
    res.append(m)


for tc in range(1, int(input()) + 1):
    N = int(input())
    input_list = list(map(int, input().rstrip().split()))
    point = input_list[:N]
    mass = input_list[N:]
    res = []
    for i in range(1, N):
        balance(point[i - 1], point[i], i, 1)

    print('#{} '.format(tc), end='')
    for r in res:
        print("{:.10f}".format(r), end=' ')
    print()
