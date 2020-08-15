T = int(input())
for t in range(1, T+1):
    N, P, T = map(int, input().split())
    if P > T:
        res1 = T
    else:
        res1 = P
    if N < P + T:
        res2 = P + T - N
    else:
        res2 = 0
    print(f'#{t} {res1} {res2}')