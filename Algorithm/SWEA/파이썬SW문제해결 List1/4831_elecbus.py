'''
K = 한번충전으로 최대한 이동할 수 있는 정류장 수
N = 종점인 정류장(정류장의 갯수)
M = 충전기가 설치된 정류장의 수
'''

def elec_bus(k, n, m, charges):
    fuel = k
    charge_count = 0
    sp = 0
    while sp != n:
        fuel -= 1
        if fuel == 0 and sp in charges:
            fuel = k
            charge_count += 1
        elif fuel == 0 and sp not in charges:
            count = k
            for j in range(sp, sp-k, -1):
                if j in charges:
                    fuel = k
                    charge_count += 1
                    sp = j
                    break
                else:
                    count -= 1
                    if count == 0:
                        return 0   
        sp += 1         
    return charge_count

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))
    print(f'#{tc} {elec_bus(K, N, M, charges)}')
    