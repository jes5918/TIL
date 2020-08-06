def binscan(last, target):
    cnt = 0
    l = 1
    r = last
    while True:
        cnt += 1
        cen = int((l + r) / 2)
        if cen > target:
            r = cen
        elif cen < target:
            l = cen
        else:
            return cnt

T =int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    x = binscan(P, A)
    y = binscan(P, B)
    if x > y:
        res = 'B'
    elif x < y:
        res = 'A'
    else:
        res = 0
    print(f'#{tc} {res}')