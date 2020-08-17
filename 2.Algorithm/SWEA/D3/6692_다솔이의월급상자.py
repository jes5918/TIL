T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = float()
    for _ in range(N):
        p, x = map(float, input().split())
        result += p * x
    print(f'#{tc} {result}')
    