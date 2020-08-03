def elec_bus(k, n, m, charges):
    fuel = k
    charge_count = 0

    for i in range(1, n+1):
        fuel -= 1
        if fuel < 0:
            return 0
        if i in charges:
            fuel = k
            charge_count += 1
            for charge

    return charge_count

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))
    print(f'#{tc} {elec_bus(K, N, M, charges)}')
    