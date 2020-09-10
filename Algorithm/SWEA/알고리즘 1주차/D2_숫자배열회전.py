def rotate90(li):
    new = [[0 for x in range(N)] for y in range(N)]
    for i in range(N):
        for j in range(N):
            new[j][N-i-1] = li[i][j]
    return new

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[str(x) for x in input().split()] for _ in range(N)]
    ro90 = rotate90(arr)
    ro180 = rotate90(ro90)
    ro270 = rotate90(ro180)
    print(f'#{tc}')
    for i in range(N):
        a = ''.join(ro90[i])
        b = ''.join(ro180[i])
        c = ''.join(ro270[i])
        print(f'{a} {b} {c}')