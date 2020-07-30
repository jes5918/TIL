for i in range(1, int(input()) + 1):
    N = int(input())
    s1 = N * (N + 1) // 2
    s3 = s1 * 2
    s2 = s3 - N
    print(f'#{i} {s1} {s2} {s3}')