for tc in range(1, int(input()) + 1):
    p, q = map(float, input().split())
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q
    result = 'YES' if s1 < s2 else 'NO'
    print(f'#{tc} {result}')