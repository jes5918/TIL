def sumK(n, k):
    cnt = 0
    for i in range(1<<len_A):
        SUM = 0
        sub = []
        for j in range(len_A):
            if i & (1<<j):
                sub.append(A[j])
                SUM += A[j]
        if SUM == k and len(sub) == n:
            cnt += 1
    return cnt

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
len_A = len(A)
for tc in range(1, T+1):
    N, K = map(int, input().split())
    print(f'#{tc} {sumK(N, K)}')