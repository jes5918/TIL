for _ in range(int(input())):
    arr = list(map(int, input().split()))
    N = arr[0]
    point = arr[1:]
    aver = sum(point) / N
    cnt = 0
    for i in range(N):
        if point[i] > aver:
            cnt += 1
    print(str('%.3f' % round(cnt/N*100, 3)) + '%')
