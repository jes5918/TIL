T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_stop = {}
    for i in range(N):
        a, b = map(int, input().split())
        for rout in range(a, b+1):
            bus_stop[rout] = bus_stop.get(rout, 0) + 1
    
    P = int(input())
    res = []
    for _ in range(P):
        res.append(int(input()))
    
    print(f'#{tc}', end=' ')
    
    for res in res:
        print(bus_stop.get(res, 0), end=' ')
    print()