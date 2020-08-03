T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    sum_li = [0] * (N-M+1)
    for i in range(0, N-M+1):
        for j in range(M):
            sum_li[i] += li[i+j]
    print(f'#{tc} {max(sum_li) - min(sum_li)}')