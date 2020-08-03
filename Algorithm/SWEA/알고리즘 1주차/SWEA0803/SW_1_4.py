T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [[int(x) for x in input().split()] for _ in range(N)]
    max_pari = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_pari = 0
            for a in range(M):
                for b in range(M):
                    sum_pari += li[i+a][j+b]
            if max_pari < sum_pari:
                max_pari = sum_pari
    print(f'#{tc} {max_pari}')