import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input().rstrip()) + 1):
    N, M = map(int, input().rstrip().split())
    A = []
    B = []
    for _ in range(N):
        A += [input().rstrip()]
    for _ in range(M):
        B += [input().rstrip()]
    cnt = 0
    for i in range(M):
        temp_B = len(B[i])
        for j in range(N):
            temp_A = len(A[j])
            if temp_A < temp_B:
                continue
            else:
                t = A[j][:temp_B]
                if B[i] == t:
                    cnt += 1
                    break

    print('#{} {}'.format(tc, cnt))