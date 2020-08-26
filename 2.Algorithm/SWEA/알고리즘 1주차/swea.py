T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [[int(i) for i in input().split()] for j in range(N)]
    max_pari = 0
    for i in range(N-M):
        for j in range(N-M):
            pari = 0
            for x in range(M):
                for y in range(M):
                    pari += li[i+x][j+y]
            if max_pari < pari:
                max_pari = pari
    print(f'#{tc} {max_pari}')
        