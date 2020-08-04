T = int(input())
for tc in range(1, T+1):
    N = int(input())
    res = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            res += i
        else:
            res -= i
    print(f'#{tc} {res}')